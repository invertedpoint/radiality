"""
storage:app
"""

import os

from core.subsystem import Storage


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')


subsystem = Storage(
    logging_config=os.path.join(CONFIGS_DIR, 'logging.yaml'),
    connection_config=os.path.join(CONFIGS_DIR, 'connection.yaml')
)


if __name__ == '__main__':
    subsystem.launch()
