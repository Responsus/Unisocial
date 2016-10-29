from flask import Flask, render_template,request,session,abort,jsonify,redirect,url_for, current_app
from flask.ext.script import Manager
from flask_mail import Mail,Message
from flask.ext.migrate import Migrate,MigrateCommand
from api.User import user_blueprint
from api.OAuth_endpoint import oauth_endpoint
from Classes.User import User, db
from Classes.login_manager_config import login_manager
from Classes.oauth_config import oauth
from pprint import pprint

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

app.secret_key = 'teste'

app.register_blueprint(user_blueprint)
app.register_blueprint(oauth_endpoint)

db.init_app(app)
login_manager.init_app(app)
oauth.init_app(app)

@app.route("/authorized/")
def authorized():
    
    return request.args.get("code")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(host="0.0.0.0",port=8080)
    #manager.run()