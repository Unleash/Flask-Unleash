import os
from UnleashClient import UnleashClient
from flask import current_app, _app_ctx_stack


class Unleash():
    def __init__(self, app=None):
        # Constants
        self.name = 'unleash_client'

        # Setup
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, self.name):
                ctx.unleash_client = self.initialize()
            return ctx.unleash_client

    def initialize(self):
        unleash_client = UnleashClient(
            url=app.config['UNLEASH_URL'],
            app_name=app.config['UNLEASH_APPNAME'],
            environment=app.config['FLASK_ENV'],
            instance_id="ucp-{}".format(os.getpid()),
            refresh_interval=app.config['UNLEASH_REFRESHINTERVAL'],
            metrics_interval=app.config['UNLEASH_METRICINTERVAL'],
            disable_metrics=app.config['UNLEASH_DISABLEMETRICS'],
            disable_registration=app.config['UNLEASH_DISABLEREGISTRATION'],
            custom_headers=app.config['UNLEASH_CUSTOMHEADERS'],
            custom_options=app.config['UNLEASH_CUSTOMOPTIONS'],
            custom_strategies=app.config['UNLEASH_CUSTOMSTRATEGIES'],
            cache_directory=app.config['UNLEASH_CACHEDIRECTORY']
        )

        unleash_client.initialize_client()

        return unleash_client

    def teardown(self):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, self.name):
            ctx.unleash_client.destroy()
