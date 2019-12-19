import os
from UnleashClient import UnleashClient
from flask import current_app, _app_ctx_stack  # type: ignore


class Unleash():
    def __init__(self, app=None):
        # Constants
        self.name = 'unleash_client'
        self.client = None

        # Setup
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.client = UnleashClient(
            url=app.config['UNLEASH_URL'],
            app_name=app.config['UNLEASH_APP_NAME'],
            environment=app.config['UNLEASH_ENVIRONMENT'],
            instance_id=app.config['UNLEASH_INSTANCE_ID'] if "UNLEASH_INSTANCE_ID" in app.config else "unleash-client-python",
            refresh_interval=app.config['UNLEASH_REFRESH_INTERVAL'] if 'UNLEASH_REFRESH_INTERVAL' in app.config else 15,
            metrics_interval=app.config['UNLEASH_METRIC_INTERVAL'] if 'UNLEASH_METRIC_INTERVAL' in app.config else 60,
            disable_metrics=app.config['UNLEASH_DISABLE_METRICS'] if 'UNLEASH_DISABLE_METRICS' in app.config else False,
            disable_registration=app.config['UNLEASH_DISABLE_REGISTRATION'] if 'UNLEASH_DISABLE_REGISTRATION' in app.config else False,
            custom_headers=app.config['UNLEASH_CUSTOM_HEADERS'] if 'UNLEASH_CUSTOM_HEADERS' in app.config else {},
            custom_options=app.config['UNLEASH_CUSTOM_OPTIONS'] if 'UNLEASH_CUSTOM_OPTIONS' in app.config else {},
            custom_strategies=app.config['UNLEASH_CUSTOM_STRATEGIES'] if 'STRATEGIES' in app.config else {},
            cache_directory=app.config['UNLEASH_CACHE_DIRECTORY'] if 'UNLEASH_CACHE_DIRECTORY' in app.config else None
        )

        self.client.initialize_client()
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['Unleash'] = self
