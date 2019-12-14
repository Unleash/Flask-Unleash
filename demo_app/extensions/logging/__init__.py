import sys

import logging
import logmatic
from demo_app.helpers.requestid import RequestIdFilter


def init_app(app):
    # pylint: disable=protected-access
    log_level = logging._nameToLevel[app.config['LOG_LEVEL']]
    log_type = app.config['LOG_FORMATTER']

    # Configure JSON filesystem log handler
    handler = logging.StreamHandler(sys.stdout)

    if log_type.upper() == 'JSON':
        handler.setFormatter(logmatic.JsonFormatter())
    else:
        #pylint: disable=line-too-long
        text_formatter = logging.Formatter('%(asctime)s - %(request_id)s - %(name)s - %(filename)s - %(levelname)s - %(message)s')
        handler.setFormatter(text_formatter)

    handler.addFilter(RequestIdFilter())

    # Configure global logging
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(log_level)

    # app.logger.addHandler(handler)
    # app.logger.setLevel(log_level)