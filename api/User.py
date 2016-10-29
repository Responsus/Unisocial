from flask import Flask,Blueprint,jsonify,request,session,abort, redirect, url_for, render_template
from flask_wtf import form
from Classes.login_manager_config import login_manager, login_user, login_required, logout_user, current_user
from Classes.oauth_config import oauth
from Classes.User import User as UserBO
from pprint import pprint

user_blueprint = Blueprint("user", __name__)

@login_manager.user_loader
def load_user(user_id):
    userBo = UserBO()
    return userBo.get_by_id(user_id)
    
@login_required
@user_blueprint.route("/user/logout/")
def logout():
     logout_user()
     return redirect(url_for("user.login"))

@user_blueprint.route("/user/dashboard/")
def dashboard():
    return '<html><head></head><body>Dashboard</body></html>'

@user_blueprint.route("/user/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        userBO = UserBO()
        user = userBO.auth_user(request.form["email"], request.form["password"])
        if user.is_authenticated == True:
            login_user(user)
            return redirect(url_for("user.dashboard")) #jsonify({"email" : request.form["email"]})
        else:
            return redirect(url_for("user.login")) #jsonify({"email" : request.form["email"]})
    
    return '<html><head></head><body>Login</body></html>'
    
@user_blueprint.route("/user/register/", methods=["POST", "GET"])
def register():
    #TODO: Criar validacao de registro de usuario
    if request.method == "POST":
        errors = ""
        
        if request.form["password"] == request.form["confirm_password"]:
           
            
            user = UserBO(type('User', (object,),{"name" : request.form["name"], 
                "email": request.form["email"],
                "password_plain_text" : request.form["password"],
                "active" : True
                }))
            
            user.create_user()
            
            return redirect(url_for("user.login"))
        else:
            errors = "Confirmacao da senha diferente de senha"
            
    else:
        return render_template("/account/register.html")
            
    

@user_blueprint.route("/user/me/", methods=["GET"])
@oauth.require_oauth()
def get():
    return jsonify({"name" : current_user.name, "email" : current_user.email})

@user_blueprint.route("/user/", methods=["PUT"])
def update():
    pass

@user_blueprint.route("/user/", methods=["POST"])
def create_user():
    novo = request.get_json()
    user = UserBO()
