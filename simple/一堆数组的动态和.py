#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test1.py
# @Author: vmture
# @Date  : 2020/8/31
# @Desc  : 一堆数组的动态和
#https://leetcode-cn.com/problems/running-sum-of-1d-array/


# 示例 1：
#
# 输入：nums = [1,2,3,4]
# 输出：[1,3,6,10]
# 解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。
# 示例 2：
#
# 输入：nums = [1,1,1,1,1]
# 输出：[1,2,3,4,5]
# 解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。
# 示例 3：
#
# 输入：nums = [3,1,2,10,1]
# 输出：[3,4,6,16,17]
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6


class Solution:
    def runningSum(self, nums) -> list:
        return list(map(lambda x: self.sum(x, nums), range(len(nums))))

    def sum(self, x, nums):
        j = 0
        for i in range(x + 1):
            j += nums[i]
        return j


class Solution2:
    def runningSum(self, nums) -> list:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
