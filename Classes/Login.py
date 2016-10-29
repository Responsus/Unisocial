from flask.jwt import JWT,jwt_required

class Login():
	id = 0
	email = ""
	senha = ""
	def __init__(self,id=0,email='',senha=''):
			self.id = id
			self.email = email
			self.senha = senha

	@jwt.authentication_handler
	def authenticate(email,senha):
		if email == "alisson" and senha == "pass":
			return Login(id=1,email="allisson")

	@jwt.user_handler
	def load_user(payload):
		if payload['user_id'] == 1:
			return Login(id=1,email='alisson')
	
