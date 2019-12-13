from flask import Flask
from flask_unleash import Unleash, current_app

app = Flask(__name__)

app.config['UNLEASH_URL'] = "https://eu.unleash-hosted.com/demo/api"
app.config['UNLEASH_APP_NAME'] = "pyIvan"
app.config['UNLEASH_ENVIRONMENT'] = "staging"
app.config['UNLEASH_CUSTOM_HEADERS'] = {'Authorization': '56907a2fa53c1d16101d509a10b78e36190b0f918d9f122d'}
unleash = Unleash(app)

@app.route('/')
def hello_world():
    context = {
        'userId': "1"
    }

    flag_value = unleash.client.is_enabled("ivan-variations", context)
    return f'Hello, World! Your feature flag is: {flag_value}'

if __name__ == '__main__':
    app.run()