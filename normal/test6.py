#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test6.py
# @Author: vmture
# @Date  : 2020/9/9
# @Desc  : 螺旋矩阵 II
# https://leetcode-cn.com/problems/spiral-matrix-ii/

# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例:
# n^2-(n-2)^2
#
# 输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
# 8 = 3^2-(3-2)^2

# 输入: 4
# 输出:
# [
#  [ 1,  2,  3,  4 ],
#  [ 12, 13, 14, 5 ],
#  [ 11, 16, 15, 6 ],
#  [ 10, 9,  8,  7 ]
# ]
# 12 = 4^2-(4-2)^2

# 输入: 5
# 输出:
# [
#  [ 1,  2,   3,   4,   5 ],
#  [ 16, 17,  18,  19,  6 ],
#  [ 15, 24,  25,  20,  7 ],
#  [ 14, 23,  22,  21,  8 ],
#  [ 13, 12,  11,  10,  9 ]
# ]
# 16 = 5^2-(5-2)^2


class Solution:
    def generateMatrix(self, n: int) -> list:
        if n == 1:
            return [1]
        list_a = [i + 1 for i in (range(n * n))]
        a = n
        b = [[i for i in range(n)]] * n
        c = 0
        d = 0
        try:
            while a > 0:
                line_num = a * a - (a - 2) * (a - 2)
                for i in range(line_num):
                    if i < a:
                        b[c][i] = list_a[d + i]
                    elif a <= i < 2 * a:
                        b[a - 1][i - a] = list_a[d + i]
                    elif 2 * a <= i < 3 * a:
                        b[i - 2 * a][a - 1] = list_a[d + i]
                    elif 3 * a <= i < 4 * a:
                        b[c][a - (i - 3 * a)] = list_a[d + i]
                d += line_num
                a -= 2
                c += 1
                print(b)
        except:
            print()
        return b


class Solution1:
    def generateMatrix(self, n: int) -> list:
        while a > 0:


print(Solution().generateMatrix(5))
