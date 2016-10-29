from flask import Flask,Blueprint,render_template,abort,redirect,url_for,request,session,jsonify, current_app
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, roles_accepted
from flask.ext.security.utils import get_hmac, verify_password, encrypt_password, login_user, logout_user
from flask.ext.security.core import current_user
import os
from werkzeug import secure_filename
from functools import wraps
from jinja2 import TemplateNotFound
from Models.Model import db, User, Role
#from Blueprints.Account import account

class IdentityRegister:
    def __init__(self, app):
        #app.register_blueprint(account)
        #Configuracoes flask-security
        app.config["SECURITY_PASSWORD_HASH"] = "pbkdf2_sha512"
        #app.config["SECURITY_LOGIN_URL"] ="/login/"
        app.config["SECURITY_PASSWORD_SALT"] = "unisocialresponsus"
        app.config["SECURITY_REGISTERABLE"] = True
        app.config["SECURITY_LOGIN_USER_TEMPLATE"] = "account/login.html"
        app.config["SECURITY_USER_IDENTITY_ATTRIBUTES"] = ("email")

        user_datastore = SQLAlchemyUserDatastore(db, User, Role)
        security = Security(app=app, datastore= user_datastore, register_blueprint = True)

        @app.route("/deny_professor/")
        @roles_accepted("professor")
        def deny_professor():
            return "Aqui somente professor"

        @app.route("/deny_aluno/")
        @roles_accepted("aluno")
        def deny_aluno():
            return "Aqui somente aluno"

        @app.route("/logout/")
        def logout():
            print logout_user()
            return redirect(url_for("login"))

        @app.route("/login/", methods=["POST"])
        def login_post():  
            user = user_datastore.get_user(str(request.form["email"]))
            if user:
                if verify_password(str(request.form["pass"]), user.password):
                    print "senha correta"
                    login_user(user)
                else:
                    print "senha errada"
            else:
                pass
            

            return render_template("account/login.html")

        
        @app.route("/register/", methods=['GET'])        
        def register():    
            return render_template("account/register.html")

        @app.route("/register/", methods=['POST'])
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

                new_user = user_datastore.create_user(name = str(request.form["nome"]),
                                           email = str(request.form["email"]),
                                           password = encrypt_password(str(request.form["pass"])))

                new_role = user_datastore.find_or_create_role(str(request.form["tipo"]))
                user_datastore.add_role_to_user(new_user, new_role)
                db.session.commit()        
        
            except Exception as e:
                print e

            return render_template("account/register.html")

        def create_role(role_name):
            pass