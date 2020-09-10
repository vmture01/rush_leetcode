#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test5.py
# @Author: vmture
# @Date  : 2020/9/3
# @Desc  : TinyURL 的加密与解密

# https://leetcode-cn.com/problems/encode-and-decode-tinyurl/

# TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，它将返回一个简化的URL http://tinyurl.com/4e9iAk.
#
# 要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。

import random


class Codec:
    _chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        self.map = {}
        self.random_chars = ''.join(random.sample(self._chars, 6))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        url = "http://tinyurl.com/"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        https://leetcode.com/problems/design-tinyurl
        """
