#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 136. 只出现一次的数字.py
# @Author: vmture
# @Date  : 2020/9/12
# @Desc  :

# https://leetcode-cn.com/problems/single-number/

# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,1]
# 输出: 1
# 示例 2:
#
# 输入: [4,1,2,1,2]
# 输出: 4


class Solution:
    def singleNumber(self, nums: list) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i


class Solution:
    def singleNumber(self, nums: list) -> int:
        for i in range(len(nums) - 1):
            nums[i + 1] = nums[i] ^ nums[i + 1]
        return nums[-1]
