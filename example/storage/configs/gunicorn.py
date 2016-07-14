"""
Gunicorn configuration file
"""

from uuid import uuid4


# Server socket

bind = ':8888'
# import multiprocessing
# workers = multiprocessing.cpu_count() * 2 + 1


# Worker processes

worker_class = 'eventlet'


# Server mechanics

user = 'ubuntu'
group = 'ubuntu'


# Logging

loglevel = 'debug'


# Server hooks

def pre_request(worker, req):
    """
    """
    req.rid = str(uuid4())
    req.query += '&rid={}'.format(req.rid)


def post_request(worker, req, environ, resp):
    """
    """
    worker.wsgi.pulse(req.rid)
