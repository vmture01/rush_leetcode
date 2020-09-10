#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test8.py
# @Author: vmture
# @Date  : 2020/9/10
# @Desc  : 全排列

# https://leetcode-cn.com/problems/permutations/

# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。

# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution:
    def permute(self, nums: list) -> list:
        l = len(nums)
        res = []

        def h(x, tmp):
            if not x:
                res.append(tmp)
                return
            for i in range(len(x)):
                h(x[:i] + x[i + 1:], tmp + [x[i]])

        h(nums, [])
        return res


print(Solution().permute([1, 2, 3]))
