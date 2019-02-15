import logging
import sys
import os

LOG_LEVEL = os.environ.get('LOG_LEVEL', default='INFO')


class MaxLevelFilter:
    def __init__(self, max_level=logging.INFO):
        self.max_level = max_level

    def filter(self, record):
        return record.levelno <= self.max_level


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        # This section creates the format template for logging messages
        "verbose": {
            "format": "%(asctime)s [%(levelname)s] %(filename)s %(funcName)s %(lineno)d: %(message)s"
        },
        "simple": {
            "format": "%(levelname)s %(message)s"
        }
    },
    "filters": {
        'max_level_info': {
            '()': MaxLevelFilter,
            'max_level': logging.INFO,
        }
    },
    "handlers": {
        # This section creates the locations where log messages will be sent
        "stdout": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "filters": ["max_level_info", ]
        },
        "stderr": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "stream": sys.stderr,
        },
    },
    "loggers": {
        # This section defines logging objects that will be called out in code
        "tunnel-utils": {
            "handlers": ["stdout", "stderr"],
            "propagate": False,
            "level": LOG_LEVEL
        },
        "": {
            "handlers": ["stdout", "stderr", ],
            "level": LOG_LEVEL
        },
    },
}
