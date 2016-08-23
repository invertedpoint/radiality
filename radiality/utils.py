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


def subsystem_freq(host, port):
    return 'ws://{host}:{port}'.format(host=host, port=str(port))


def fail_connection():
    print('[!] Connection closed')


def fail_event(event):
    print('[!] Unknown event: {0}'.format(event))


def fail_in_signal():
    print('[!] Invalid in-signal: could not decode the signal body')


def fail_out_signal():
    print('[!] Invalid out-signal: could not decode the signal body')
