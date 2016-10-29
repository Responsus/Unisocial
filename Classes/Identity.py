from flask import Flask
from Models.Model import db, User, Role
from flask.ext.security.utils import get_hmac, verify_password
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required

#class Identity:
#    def __init__(self, app):
        #self.user_datastore = SQLAlchemyUserDatastore(db, User, Role)
        #self.security = Security(app, self.user_datastore)

app = Flask(__name__)
app.config["SECURITY_PASSWORD_HASH"] = "pbkdf2_sha512"
app.config["SECURITY_PASSWORD_SALT"] = "unisocialresponsus"
app.config["SECURITY_REGISTERABLE"] = True
app.config["SECURITY_USER_IDENTITY_ATTRIBUTES"] = ("email", "id")
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
