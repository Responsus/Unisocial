from flask import json, jsonify
from run_test import app
from Models.Identity import User as UserModel
from Classes.User import User, db
from datetime import datetime
import unittest, uuid

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User(type('User', (object,),{"name" : "teste user", 
        "email": "teste@teste.com",
        "password_plain_text" : "1234",
        "active" : False
        }))
        self.app = app
        db.init_app(self.app)

        with self.app.app_context():
            db.create_all()

    def test_ShouldVerifyPassword(self):
        password_hash = self.user.encrypt_password(self.user.password_plain_text)
        self.assertEqual(True, self.user.verify_password(self.user.password_plain_text, password_hash))

    def test_ShouldFailVerifyPassword(self):
        password_hash = self.user.encrypt_password(self.user.password_plain_text)
        self.assertEqual(False, self.user.verify_password("Wrong pass", password_hash))

    def test_create_user(self):
        user = User(self.user)

        with self.app.app_context():

            created_user = user.create_user()
            self.assertGreater(created_user.id, user.id)
            
            self.assertEqual(created_user.created_date, datetime.now().date())

            find_user_id = user.get_by_id(created_user.id)

            self.assertEqual(find_user_id.id, created_user.id)

            find_user = user.get_by_email(user.email)
            self.assertEqual(find_user.email, user.email)

    def test_alter_user(self):
         with self.app.app_context():
             userBO = User(self.user)
             user = userBO.create_user()
             self.assertEqual(user.name, self.user.name)

             user.name = "Novo user"
             user.email = "novo_email@email.com"
             user = userBO.update(user)

             self.assertEqual(user.name, "Novo user")
             self.assertEqual(user.email, "novo_email@email.com")

    def test_should_confirm_email(self):
        with self.app.app_context():
            userBO = User(self.user)
            user = userBO.create_user()
            self.assertEqual(user.name, self.user.name)
            self.assertEqual(user.email_confirmed, False)
            user.email_confirmed = True
            user = userBO.confirm_email(user.id)
            self.assertEqual(user.email_confirmed, True)
               
    def test_should_auth_user(self):
         with self.app.app_context():
              created_user = self.user.create_user()
              created_user = created_user.auth_user(self.user.email, self.user.password_plain_text)
              self.assertEqual(True, created_user.is_authenticated)
              
              created_user = created_user.auth_user(self.user.email, "Wrong Pass")
              self.assertEqual(True, created_user.is_anonymous)
