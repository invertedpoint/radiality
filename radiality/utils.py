"""
radiality:radiality.utils

The `radiality/utils.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import yaml


MSG_TIMEOUT = 1800  # 1800 sec
MSG_MAX_SIZE = 12 * 2 ** 20  # 12 MB


def subsystem_freq(host, port, point=None):
    if not point:
        point = '{host}:{port}'.format(host=host, port=port)

    return '{scheme}://{point}'.format(scheme='ws', point=point)


def load_config(config_path):
    with open(config_path, 'rt') as config_file:
        config = yaml.safe_load(config_file.read())

    return config
