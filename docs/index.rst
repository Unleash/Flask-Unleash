****************************************
Flask-Unleash Documentation
****************************************

Welcome to the Flask-Unleash pluginm documentation!  This plugin makes integrating the `Python Unleash client <https://github.com/unleash/unleash-client-python>`_ into quick and easy.

Pre-requisites
#######################################

To try out Flask-Unleash, you'll need an instance of the `Unleash <http://github.com/unleash/unleash>`_ server.  You can either use:

* Spin up a stack in Docker Compose using `unleash-docker <https://github.com/Unleash/unleash-docker>`_
* Check out the demo at `<Unleash-Hosted <https://www.unleash-hosted.com/>`_

Quickstart
#######################################

Install Flask-Unleash using pip.

.. code-block:: shell

    pip install Flask-Unleash


Next, add Flask-Unleash to your code.

.. code-block:: python

    from flask import Flask
    from flask_unleash import Unleash

    app = Flask(__name__)
    app.config["UNLEASH_URL"] = "http://localhost:4242/api"
    app.config["UNLEASH_APP_NAME"] = "demoapp"
    unleash = Unleash(app)

Now you can use the client to check feature flags

.. code-block:: python

    flag_value_1 = unleash.client.is_enabled("simple-feature")

    # You can pass in a context object (https://unleash.github.io/docs/unleash_context) for more complex features.
    context = {
        'userId': 'hamster@hamster.com'
    }
    flag_value_2 = unleash.client.is_enabled("complex-feature", context)


Check out the `demo app <https://github.com/Unleash/Flask-Unleash/tree/main/demo_app>`_ for a more real-life sample implementation.

Configuration
#######################################

.. csv-table:: Flask-Unleash Configuration
   :file: ./config.csv
   :header-rows: 1


.. Hidden TOCs

.. toctree::
    :maxdepth: 2
    :hidden:

    api
    development
    changelog
