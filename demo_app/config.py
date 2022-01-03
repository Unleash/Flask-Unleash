class BaseConfig():
    # Unleash
    UNLEASH_URL = "https://app.unleash-hosted.com/demo/api"
    UNLEASH_APP_NAME = "pyIvan"
    UNLEASH_ENVIRONMENT = "staging"
    UNLEASH_CUSTOM_HEADERS = {'Authorization': '56907a2fa53c1d16101d509a10b78e36190b0f918d9f122d'}

    # Logging
    LOG_LEVEL = "DEBUG"
    LOG_FORMATTER = "TEXT"


def config_flask(app):
    app.config.from_object(BaseConfig())
