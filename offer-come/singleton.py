#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
单例模式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/4/8
"""


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    a = 1


class Singleton2(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Singleton2, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Singleton2):
    pass


def singleton(cls, *args, **kwargs):
    instance = {}

    def getinstance():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getinstance()


@singleton
class MyClass3(object):
    pass


class MetaSingleton(type):
    def __init__(cls, *args, *kwargs):
        cls.__instance = None
        super.__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class MySingleClass1(metaclass=MetaSingleton):
    def __init__(self):
        print("singleton")


if __name__ == "__main__":
    pass
