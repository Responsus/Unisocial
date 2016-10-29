from flask import Flask,Blueprint,render_template,abort,session, request
from Classes.oauth_config import oauth
from Classes.login_manager_config import login_required, current_user
from Models.Identity import db, User, Client
from pprint import pprint

oauth_endpoint = Blueprint('oauth_endpoint',__name__,template_folder='templates')

@oauth_endpoint.route('/oauth/authorize/', methods=['GET', 'POST'])
@login_required
@oauth.authorize_handler
def authorize(*args, **kwargs):
    if request.method == 'GET':
        client_id = kwargs.get('client_id')
        client = Client.query.filter_by(client_id=client_id).first()
        kwargs['client'] = client
        return render_template('/oauth/oauthorize.html', user= current_user, **kwargs)

    confirm = request.form.get('confirm', 'no')
    return confirm == 'yes'
    
@oauth_endpoint.route('/oauth/token/', methods=["POST"])
@oauth.token_handler
def access_token():
    return None