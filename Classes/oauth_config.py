from datetime import datetime, timedelta
from Classes.login_manager_config import login_required, current_user
from Models.Identity import db, User as UserModel, Client, Grant, Token
from flask_oauthlib.provider import OAuth2Provider

oauth = OAuth2Provider()


@oauth.clientgetter
def load_client(client_id):
    return Client.query.filter_by(client_id=client_id).first()
    
@oauth.grantgetter
def load_grant(client_id, code):
    return Grant.query.filter_by(client_id=client_id, code=code).first()

@oauth.grantsetter
def save_grant(client_id, code, request, *args, **kwargs):
    # decide the expires time yourself
    expires = datetime.utcnow() + timedelta(seconds=100)
    grant = Grant(
        client_id=client_id,
        code=code['code'],
        redirect_uri=request.redirect_uri,
        _scopes=' '.join(request.scopes),
        user=UserModel.query.filter(UserModel.id == current_user.id).first(),
        expires=expires
    )
    db.session.add(grant)
    db.session.commit()
    return grant
    
@oauth.tokengetter
def load_token(access_token=None, refresh_token=None):
    if access_token:
        return Token.query.filter_by(access_token=access_token).first()
    elif refresh_token:
        return Token.query.filter_by(refresh_token=refresh_token).first()

@oauth.tokensetter
def save_token(token, request, *args, **kwargs):
    toks = Token.query.filter_by(client_id=request.client.client_id,
                                 user_id=request.user.id)
    # make sure that every client has only one token connected to a user
    for t in toks:
        db.session.delete(t)

    expires_in = token.get('expires_in')
    expires = datetime.utcnow() + timedelta(seconds=expires_in)

    tok = Token(
        access_token=token['access_token'],
        refresh_token=token['refresh_token'],
        token_type=token['token_type'],
        _scopes=token['scope'],
        expires=expires,
        client_id=request.client.client_id,
        user_id=request.user.id,
    )
    db.session.add(tok)
    db.session.commit()
    return tok