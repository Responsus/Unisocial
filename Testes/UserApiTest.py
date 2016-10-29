from flask import json, jsonify, url_for

from flask_login import current_user
from run_test import app, db, login_manager
from Models.Identity import User as UserModel, Client
from Classes.User import User, db
import unittest, uuid
from pprint import pprint

class UserApiTest(unittest.TestCase):
    def setUp(self):
        self.user = User(type('User', (object,),{"name" : "teste user", 
        "email": "teste@teste.com",
        "password_plain_text" : "1234",
        "active" : True
        }))
        
        self.app = app
        #db.init_app(self.app)
        #login_manager.init_app(self.app)
        with self.app.app_context():
            db.create_all()
            
    def tearDown(self):
        with self.app.app_context():
            db.drop_all()
        
    
    def create_user(self):
        with self.app.app_context():
            self.user = self.user.create_user()
            
    def test_should_login_user(self):
         with self.app.app_context():
            self.create_user()
            with app.test_client() as c:
                resp = c.post('/user/login/', 
                    data=dict(email = self.user.email, password = "1234"))
                
                self.assertEqual(resp.status_code, 302)
                self.assertEqual(resp.location, url_for('user.dashboard', _external=True))
                
                self.assertEqual(True, current_user.is_authenticated)
                
                resp = c.get('/user/logout/')
                
                resp = c.post('/user/login/', 
                    data=dict(email = self.user.email, password = "Wrong Pass"))
                    
                self.assertEqual(resp.status_code, 302)
                self.assertEqual(resp.location, url_for('user.login', _external=True))
                self.assertEqual(False, current_user.is_authenticated)
                
                resp = c.post('/user/login/', 
                    data=dict(email = "wrong@email.com", password = "1234"))
                    
                self.assertEqual(resp.status_code, 302)
                self.assertEqual(resp.location, url_for('user.login', _external=True))
                self.assertEqual(False, current_user.is_authenticated)
    
    def test_should_register_user(self):
        with self.app.app_context():
            with app.test_client() as c:
                resp = c.post('/user/register/',
                        data=dict(name = self.user.name, email = self.user.email,
                                  password = self.user.password_plain_text, confirm_password = self.user.password_plain_text))
                
                self.assertEqual(resp.status_code, 302)
                self.assertEqual(resp.location, url_for('user.login', _external=True))
                
                user = User().get_by_email(self.user.email)
                self.assertEqual(hasattr(user, 'id'), True)
                
    def test_should_request_register_page(self):
        with self.app.app_context():
            with app.test_client() as c:
                resp = c.get('/user/register/')
                self.assertEqual(("Registrar" in resp.data), True)
                
            
    def test_should_login_user_api(self):
        with self.app.app_context():
            self.create_user()
            with app.test_client() as c:
                pass
               #efetua login usuario
              # c.post('/user/login/', 
              #      data=dict(email = self.user.email, password = "1234"))
                    
               #resp = c.get('/user/me/')
              # data = json.loads(resp.data)
              # self.assertEqual("teste user", data["name"])