from flask import Flask,Blueprint,render_template,abort,redirect,url_for,request,session,jsonify, current_app
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required
from flask.ext.security.utils import get_hmac, verify_password, encrypt_password
import os
from werkzeug import secure_filename
from functools import wraps
from jinja2 import TemplateNotFound
from Models.Model import db, User, Role

account = Blueprint('account',__name__,template_folder='templates')
app = Flask(__name__)


#user_datastore = SQLAlchemyUserDatastore(db, User, Role)
#security = Security(app, user_datastore)

@account.route("/login/", methods=["GET"])
def login():
    print encrypt_password("aaa")
    return render_template("account/login.html")

@account.route("/login/", methods=["POST"])
def login_post():
    try:
        #user = user_datastore.get_user(str(request.form["email"]))
        user = user_datastore.find_user(email = str(request.form["email"]),
                                        password = str(request.form["pass"]))
        return user.name
    except Exception as e :
        print e
        return False
    

@account.route("/logout/")
def logout():
    pass

@account.route("/register/", methods=['GET'])
def register():    
    return render_template("account/register.html")

@account.route("/register/", methods=['POST'])
def register_post():
    try:

        #TODO: Validacao server side
        #cryptado = encrypt_password("segredo") #sha256_crypt.encrypt("toomanysecrets")
        #print len(cryptado)
        #print cryptado
        #print verify_password("aaaaa", "aaaaa")
        #user_datastore.create_user(name = request.form["nome"],
        #                           email = request.form["email"],
        #                           password =encrypt_password(request.form["pass"]))

        user_datastore.create_user(name = str(request.form["nome"]),
                                   email = str(request.form["email"]),
                                   password = str(request.form["pass"]))
        db.session.commit()        
        
    except Exception as e:
        print e

    return render_template("account/register.html")

@account.route("/profile/")
@login_required
def profile():
    pass
    