"""
radiality:radiality.utils

The `radiality/utils.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import os
import logging
import logging.config

import yaml


class Logger:
    """
    Logging
    """
    _applog = None  # logger instance

    def __init__(self, configs_dir):
        """
        Setups the logging configuration
        """
        path = os.path.join(configs_dir, 'logging.yaml')

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
