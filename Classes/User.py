from Models.Identity import db, User as UserModel
from Classes.login_manager_config import UserMixin, AnonymousUserMixin
from passlib.hash import bcrypt
from datetime import datetime
import uuid
from pprint import pprint

class User(UserMixin):
    def __init__(self, user=None):
        if user is not None:
            self.id = user.id if hasattr(user, 'id') else 0
            self.name = user.name if hasattr(user, 'name') else ''
            self.email = user.email if hasattr(user, 'email') else ''
            self.active = user.active if hasattr(user, 'active') else False
            self.password_plain_text =  user.password_plain_text if hasattr(user, 'password_plain_text') else ''
            self.password_hash = user.password_hash if hasattr(user, 'password_hash') else ''
            self.email_confirmed = user.email_confirmed if hasattr(user, 'email_confirmed') else False
            self.created_date = user.created_date if hasattr(user, 'created_date') else datetime.min
            #self.is_authenticated = True
            #self.is_anonymous = False
        #else:
        #    self.is_authenticated = False
        #    self.is_anonymous = True
        #    self.id = None
            

    def create_user(self):
        try:
            user = UserModel(self)
            user.password_hash = self.encrypt_password(self.password_plain_text)
            user.active = True
            user.email_confirmed = False
            user.created_date = datetime.now().date()
            db.session.add(user)
            db.session.commit()
            return User(user)
        except Exception as e:
            print "Erro ao criar usuario %", e
            raise e

    def update(self, entity):
        try:
            user = UserModel.query.filter(UserModel.id == entity.id).first()
            user.name = entity.name
            user.email = entity.email
            db.session.commit()
            return user
        except Exception as e:
            print "Erro ao salvar usuario %", e
            raise e
    
    def auth_user(self, email, password):
        user = self.get_by_email(email)
        if hasattr(user, 'password_hash'):
            if self.verify_password(password, user.password_hash):
                #user.is_authenticated = True
                return user
        
        return AnonymousUserMixin()

    def encrypt_password(self, password):
        return bcrypt.encrypt(password)

    def verify_password(self, password, password_hash):
        return bcrypt.verify(password, password_hash)

    def get_by_id(self, id):
        return User(UserModel.query.filter(UserModel.id == id).first())

    def get_by_email(self, email):
        return  User(UserModel.query.filter(UserModel.email == email).first())

    def confirm_email(self, user_id):
        try:
            user = UserModel.query.filter(UserModel.id == user_id).first()
            user.email_confirmed = True
            db.session.commit()
            return User(user)
        except Exception as e:
            print "Erro ao confirmar email do usuario %", e
            raise e
            
    def is_active(self):
        return self.active
        
    def get_id(self):
        return self.id
