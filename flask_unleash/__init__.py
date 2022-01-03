import os
from UnleashClient import UnleashClient
from flask import current_app, _app_ctx_stack  # type: ignore


CONFIG_MAPPING = {
    'UNLEASH_INSTANCE_ID': 'instance_id',
    'UNLEASH_REFRESH_INTERVAL': 'refresh_interval',
    'UNLEASH_REFRESH_JITTER': 'refresh_jitter',
    'UNLEASH_METRIC_INTERVAL': 'metrics_interval',
    'UNLEASH_METRIC_JITTER': 'metrics_jitter',
    'UNLEASH_DISABLE_METRICS': 'disable_metrics',
    'UNLEASH_DISABLE_REGISTRATION': 'disable_registration',
    'UNLEASH_CUSTOM_HEADERS': 'custom_headers',
    'UNLEASH_CUSTOM_OPTIONS': 'custom_options',
    'UNLEASH_CUSTOM_STRATEGIES': 'custom_strategies',
    'UNLEASH_CACHE_DIRECTORY': 'cache_directory',
    'UNLEASH_PROJECT_NAME': 'project_name',
    'UNLEASH_VERBOSE_LOG_LEVEL': 'verbose_log_level'
}


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
        # Populate required arguments.
        unleash_args = {
            'url': app.config['UNLEASH_URL'],
            'app_name': app.config['UNLEASH_APP_NAME'],
            'environment': app.config['UNLEASH_ENVIRONMENT']
        }

        # Populate optional arguments.
        populated_optional_args = filter(lambda x: x in app.config, CONFIG_MAPPING.keys())
        for option in populated_optional_args:
            unleash_args[CONFIG_MAPPING[option]] = app.config[option]

        # Set up client.
        self.client = UnleashClient(**unleash_args)

        self.client.initialize_client()
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['Unleash'] = self
