def init_app(app, **kwargs):
    from . import resources

    app.register_blueprint(resources.check_blueprint)