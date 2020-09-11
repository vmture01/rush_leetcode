#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test9.py
# @Author: vmture
# @Date  : 2020/9/10
# @Desc  : 括号生成

# https://leetcode-cn.com/problems/generate-parentheses/

# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#  
#
# 示例：
#
# 输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
# 左括号的数目一旦小于右括号的数目，以及，左括号的数目和右括号数目均小于n。


class Solution:
    # 超时
    def generateParenthesis(self, n: int) -> list:
        init = "()" * n
        res = []

        def h(x, tmp):
            if not x and ''.join(tmp) not in res:
                res.append(''.join(tmp))
                return
            for i in range(len(x)):
                if tmp.count("(") >= tmp.count(")"):
                    h(x[:i] + x[i + 1:], tmp + [x[i]])

        h(list(init), [])
        return res


class Solution1:
    # 超时
    def generateParenthesis(self, n: int) -> list:
        res = []
        chart = ""

        def h(charts, left, right):
            if left == 0 and right == 0:
                res.append(charts)
                return
            if left > right:
                return
            if left > 0:
                h(charts + "(", left - 1, right)
            if right > 0:
                h(charts + ")", left, right-1)

        h("", n, n)
        return res


print(Solution1().generateParenthesis(2))

# c = ''.join(i for i in ['(', ')', '(', ')'])
# m = 0
# for i in range(2):
#     if not c.replace("()", ""):
#         m = 2
#     elif c != c.replace("()", ""):
#         m += 1
#         c = c.replace("()", "")
#         print(c)
#     else:
#         break
# print(m)
