#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test7.py
# @Author: vmture
# @Date  : 2020/9/10
# @Desc  : 子集

# https://leetcode-cn.com/problems/subsets/

# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution:
    def subsets(self, nums: list) -> list:
        arr = [[], nums]
        num = (len(nums) * (len(nums) + 1)) / 2
        for i in range(int(num)):
            if i < len(nums):
                arr.append(nums[i])
            else:
                n = int(i / len(nums))
                l = i % (len(nums))

        return arr


class Solution1:
    # 迭代
    def subsets(self, nums: list) -> list:
        arr = [[]]
        for i in nums:
            a = [[i] + num for num in arr]
            arr += a
        return arr


class Solution2:
    # 回溯
    # 其实回溯算法关键在于:不合适就退回上一步
    #
    # 然后通过约束条件, 减少时间复杂度.
    def subsets(self, nums: list) -> list:
        res = []
        l = len(nums)

        def help(x, tmp):
            res.append(tmp)
            for i in range(x, l):
                help(i + 1, tmp + [nums[i]])

        help(0, [])
        return res


# print(Solution1().subsets([1, 2, 3, 4]))
print(Solution2().subsets([1, 2, 3, 4]))
