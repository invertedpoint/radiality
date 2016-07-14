"""
radiality:radiality.utils

The `radiality/utils.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import os
import logging
import logging.config

import yaml


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')
URL_PROTOCOL = 'http'


class Logger:
    """
    Logging
    """
    _applog = None  # logger instance

    def __init__(self):
        """
        Setups the logging configuration
        """
        path = os.path.join(CONFIGS_DIR, 'logging.yaml')

        if os.path.exists(path):
            with open(path, 'rt') as config_file:
                config = yaml.safe_load(config_file.read())
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=logging.INFO)

        self._applog = logging.getLogger('core.app')

    def applog(self):
        """
        Returns the current logger for the application
        """
        return self._applog
