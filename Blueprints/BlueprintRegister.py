from Blueprints.Account import account

class BluePrintRegister:
    def __init__(self, app):
        app.register_blueprint(account)