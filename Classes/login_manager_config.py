from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin, AnonymousUserMixin

login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.anonymous_user = AnonymousUserMixin