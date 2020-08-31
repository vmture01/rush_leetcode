#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test2.py
# @Author: vmture
# @Date  : 2020/8/31
# @Desc  : 好数对的数目
# https://leetcode-cn.com/problems/number-of-good-pairs/
# 阶加 https://baike.baidu.com/item/%E9%98%B6%E5%8A%A0/3160625?fr=aladdin


# 给你一个整数数组 nums 。
#
# 如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。
#
# 返回好数对的数目。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3,1,1,3]
# 输出：4
# 解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始
# 示例 2：
#
# 输入：nums = [1,1,1,1]
# 输出：6
# 解释：数组中的每组数字都是好数对
# 示例 3：
#
# 输入：nums = [1,2,3]
# 输出：0
#  
#
# 提示：
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

class Solution:
    def numIdenticalPairs(self, nums: list) -> int:
        result = 0
        for i in range(len(nums)):
            if nums.count(nums[i]) <= 1:
                continue
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    result += 1
        return result


class Solution2:
    def numIdenticalPairs(self, nums: list) -> int:
        result = 0
        n = set(nums)
        for i in n:
            s = nums.count(i)
            result += s * (s - 1) / 2
        return int(result)


print(Solution2().numIdenticalPairs([1, 2, 3, 1, 1, 3]))
