from flask import json, jsonify, url_for, json
from Classes.login_manager_config import login_manager, login_user, login_required, logout_user, current_user
from run_test import app, db
from Models.Identity import User as UserModel, Client
from Classes.ClientApi import ClientApi
from Classes.User import User, db
import unittest, uuid
from flask_oauthlib.client import OAuth
from pprint import pprint

class ClientApiTest(unittest.TestCase):
    def setUp(self):
        self.user = User(type('User', (object,),{"name" : "teste user", 
        "email": "teste@teste.com",
        "password_plain_text" : "1234",
        "active" : True
        }))
        
        self.client = Client()
        
        self.client.name = "App test"
        self.client.description = "Um app de test"
        self.client.is_confidential = True
        self.client._default_scopes = "email"
        self.client._redirect_uris = "http://localhost:8080/authorized/"
        
        self.app = app
        #db.init_app(self.app)
        #login_manager.init_app(self.app)

        with self.app.app_context():
            db.create_all()
            self.user = self.user.create_user()
    
    def tearDown(self):
        with self.app.app_context():
            db.drop_all()
    
    #metodo utilizado para facilitar outros testes
    def create_client_api(self): 
        clientBo = ClientApi()
        self.new_client = clientBo.create(self.client)
    
    def test_should_create_client_api(self):
        with self.app.app_context():
            clientBo = ClientApi()
            
            new_client = clientBo.create(self.client)
            self.assertNotEqual(new_client.client_secret, "")
            
    def test_should_authorize_client(self):
        with self.app.app_context():
            with app.test_client() as c:
                self.create_client_api()
                
                
                login_resp = c.post('/user/login/', 
                    data=dict(email = self.user.email, password = "1234"))
                
                self.assertEqual(login_resp.status_code, 302)
                self.assertEqual(login_resp.location, url_for('user.dashboard', _external=True))
                
                get_resp = c.get("/oauth/authorize/",
                    data=dict(client_id=self.new_client.client_id, response_type="code"))
                 
                self.assertEqual(get_resp.status_code, 200)
                
                post_resp = c.post("/oauth/authorize/", 
                    data=dict(confirm = "yes", scope = self.new_client._default_scopes,
                                response_type="code", redirect_uri = self.new_client.redirect_uris,
                                client_id=self.new_client.client_id
                            ), follow_redirects=True)
                            
                authorization_code = post_resp.data
                
                self.assertEqual(post_resp.status_code, 200)
                self.assertNotEqual("", authorization_code)
                
                post_resp = c.post("/oauth/token/", 
                    data=dict(grant_type="authorization_code",
                            code = authorization_code,
                            client_id = self.new_client.client_id,
                            client_secret = self.new_client.client_secret,
                            redirect_uri = self.new_client.redirect_uris
                        ), follow_redirects=True)
                        
                token = json.loads(post_resp.data)
                
                get_resp = c.get("/user/me/", headers={"Authorization": "Bearer " + token['access_token']})
                self.assertEqual(get_resp.status_code, 200)
                
                get_resp = c.get("/user/me/", headers={"Authorization": "Bearer wrong-token-999999"})
                self.assertEqual(get_resp.status_code, 401)