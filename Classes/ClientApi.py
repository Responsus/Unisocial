from Models.Identity import db, Client
from werkzeug.security import gen_salt
import uuid

class ClientApi:
    def create(self, new_client):
        client = Client()
        client.name = new_client.name
        client.description = new_client.description
        client.is_confidential = new_client.is_confidential
        client.client_secret = gen_salt(50)
        client.user_id = new_client.user_id
        client.client_id = gen_salt(40)
        client._redirect_uris = new_client._redirect_uris
        client._default_scopes = new_client._default_scopes
        db.session.add(client)
        db.session.commit()
        
        return client