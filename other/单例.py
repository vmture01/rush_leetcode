#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 单例.py
# @Author: vmture
# @Date  : 2020/9/18
# @Desc  :


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class Spam(metaclass=Singleton):
    def __new__(cls):
        return super().__new__(cls)

    def __init__(self):
        self.param = 123


class A:
    def __init__(self):
        print(123)

    # if __name__ == '__main__':
    a = Spam()
    a.param = 222
    print(a.param)
    b = Spam()
    print(b.param)
