from flask import g


def log_a():
    print('log a %s' % g.username)

def log_b():
    print('log b %s' % g.username)
