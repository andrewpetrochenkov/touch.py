#!/usr/bin/env python
import os
import public
import values


def _fullpath(path):
    return os.path.abspath(os.path.expanduser(path))


def _mkdir(path):
    if path.find("/") > 0 and not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))


def _utime(path):
    try:
        os.utime(path, None)
    except Exception:
        open(path, 'a').close()


@public.add
def touch(path):
    """mkdir + touch path(s)"""
    for path in values.get(path):
        if path:
            path = _fullpath(path)
            _mkdir(path)
            _utime(path)
