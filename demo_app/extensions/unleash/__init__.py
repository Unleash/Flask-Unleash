from flask_unleash import Unleash

UNLEASH = Unleash()

def init_app(app):
    UNLEASH.init_app(app)
