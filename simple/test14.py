#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test14.py
# @Author: vmture
# @Date  : 2020/9/10
# @Desc  : 汉明距离

# https://leetcode-cn.com/problems/hamming-distance/

# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
#
# 注意：
# 0 ≤ x, y < 231.
#
# 示例:
#
# 输入: x = 1, y = 4
#
# 输出: 2
#
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# 上面的箭头指出了对应二进制位不同的位置。

class Solution:
    # 通过^按位异或运算符求两个数的按位异或,再计算多少个1
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")
