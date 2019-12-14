from . import logging
from . import unleash

def init_app(app):
    extensions = [
        logging,
        unleash
    ]

    for extension in extensions:
        extension.init_app(app)
