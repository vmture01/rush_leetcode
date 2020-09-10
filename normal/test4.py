#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test4.py
# @Author: vmture
# @Date  : 2020/9/3
# @Desc  : 交换数字

# 编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。
#
# 示例：
#
# 输入: numbers = [1,2]
# 输出: [2,1]
# 提示：
#
# numbers.length == 2


class Solution:
    def swapNumbers(self, numbers):
        numbers.append(numbers[0])
        return numbers[1:]


class Solution1:
    def swapNumbers(self, numbers):
        numbers[0], numbers[1] = numbers[1], numbers[0]
        return numbers
