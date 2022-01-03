from flask import Flask, make_response, jsonify
from demo_app.config import config_flask
from demo_app.helpers.requestid import requestid


def create_app():
    app = Flask(__name__)

    from demo_app import extensions
    from demo_app import modules

    config_flask(app)
    extensions.init_app(app)
    modules.init_app(app)

    @requestid
    @app.errorhandler(500)
    def internal_error(exception):  # pylint: disable=W0612
        app.logger.error(exception)  # pylint: disable=E1101
        return make_response(jsonify(exception), 500)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
