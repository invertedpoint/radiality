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
            logging.basicConfig(level=logging.DEBUG)

        self._applog = logging.getLogger('core.app')

    def applog(self):
        """
        Returns the current logger for the application
        """
        return self._applog


class Loggable:
    """
    Mixin for the capability of being recorded in a log
    """
    _logger = None

    def log(self, msg, *args, **kwargs):
        """
        Logs the info message
        """
        self._logger.info(msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        """
        Logs the warning message
        """
        self._logger.warning(msg, *args, **kwargs)

    def fail(self, msg, *args, **kwargs):
        """
        Logs the error message
        """
        self._logger.error(msg, *args, **kwargs)


def subsystem_freq(host, port):
    return 'ws://{host}:{port}'.format(host=host, port=str(port))
