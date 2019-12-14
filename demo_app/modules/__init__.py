from . import check

def init_app(app, **kwargs):
    modules = [
        check
    ]

    for module in modules:
        module.init_app(app)