# Flask-Unleash

![](https://github.com/unleash/flask-unleash/workflows/CI/badge.svg?branch=main) [![Coverage Status](https://coveralls.io/repos/github/Unleash/Flask-Unleash/badge.svg?branch=main)](https://coveralls.io/github/Unleash/Flask-Unleash?branch=main) [![PyPI version](https://badge.fury.io/py/flask-unleash.svg)](https://badge.fury.io/py/flask-unleash) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flask_unleash) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Flask extension to make using Unleash that much easier! 🚦🚦🚦  This plugin makes integrating the [Python Unleash client](https://github.com/unleash/unleash-client-python) into quick and easy.

* [Documentation](https://unleash.github.io/Flask-Unleash/)
* [Changelog](https://docs.getunleash.io/Flask-Unleash/changelog.html)

## Pre-requisites

To try out Flask-Unleash, you'll need an instance of the [Unleash](http://github.com/unleash/unleash) server.  You can either use:
* Spin up a stack in Docker Compose using [unleash-docker](https://github.com/Unleash/unleash-docker)
* Check out the demo at [Unleash-Hosted](https://www.unleash-hosted.com/)

## Quickstart
Install Flask-Unleash using pip.

```python
pip install Flask-Unleash
```

Next, add Flask-Unleash to your code.

```Python
from flask import Flask
from flask_unleash import Unleash

app = Flask(__name__)
app.config["UNLEASH_URL"] = "http://localhost:4242/api"
app.config["UNLEASH_APP_NAME"] = "demoapp"
unleash = Unleash(app)
```

Now you can use the client to check feature flags
```Python
flag_value_1 = unleash.client.is_enabled("simple-feature")

# You can pass in a context object (https://unleash.github.io/docs/unleash_context) for more complex features.
context = {
    'userId': 'hamster@hamster.com'
}
flag_value_2 = unleash.client.is_enabled("complex-feature", context)
```

Check out the [demo app](https://github.com/Unleash/Flask-Unleash/tree/main/demo_app) for a more real-life sample implementation.

## Configuring Flask-Unleash

See the [Flask-Unleash documentation](https://docs.getunleash.io/Flask-Unleash/) for information about configuring Unleash.
