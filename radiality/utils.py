"""
radiality:radiality.utils

The `radiality/utils.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import yaml


def subsystem_freq(host, port):
    return 'ws://{host}:{port}'.format(host=host, port=str(port))


def load_config(config_path):
    with open(config_path, 'rt') as config_file:
        config = yaml.safe_load(config_file.read())

    return config
