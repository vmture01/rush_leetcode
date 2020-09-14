#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 238. 除自身以外数组的乘积.py
# @Author: vmture
# @Date  : 2020/9/12
# @Desc  :

# https://leetcode-cn.com/problems/product-of-array-except-self/

#
# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
#  
#
# 示例:
#
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]

# 1:   0001
# 2:   0010
# 3:   0011
# 4:   0100
#  
# 24: 11000
# 12:  0110
# 8:   1000
# 6:   0110

#
# 提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
#
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

class Solution:
    def productExceptSelf(self, nums: list) -> list:
        length = len(nums)
        res = []

        def h(nums1, length1):
            a = 1
            if length1 == length:
                return
            for i in nums1:
                a *= i
            res.append(a)
            length1 += 1
            h(nums[:length1] + nums[length1 + 1:], length1)

        h(nums[1:], 0)
        return res


class Solution1:
    def productExceptSelf(self, nums: list) -> list:
        res, p, q = [1], 1, 1
        for i in range(len(nums) - 1):  # bottom triangle
            print("i:%s" % i)
            p *= nums[i]
            res.append(p)
            print("p:%s" % p)
            print("res:%s" % res)

        for i in range(len(nums) - 1, 0, -1):  # top triangle
            print("i:%s" % i)
            q *= nums[i]
            res[i - 1] *= q
            print("q:%s" % q)
            print("res:%s" % res)
        return res


print(Solution1().productExceptSelf([1, 2, 3, 4]))
