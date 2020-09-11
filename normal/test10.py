#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test10.py
# @Author: vmture
# @Date  : 2020/9/11
# @Desc  : 比特位计数

# https://leetcode-cn.com/problems/counting-bits/

# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
#
# 示例 1:
#
# 输入: 2
# 输出: [0,1,1]
# 示例 2:
#
# 输入: 5
# 输出: [0,1,1,2,1,2]

# 1 :[0001]
# 2 :[0010]
# 3 :[0011]
# 4 :[0100]
# 5 :[0101]
# 6 :[0110]
# 7 :[0111]
# 8 :[1000]
# 9 :[1001]
# 偶数 f(n)=f(n/2)*10
# 奇数 f(n)=f(n-1)+1
#
#


class Solution:
    def countBits(self, num: int) -> list:
        res = [0]
        for i in range(1, 1 + num):
            if i % 2 == 0:
                res.append(res[int(i / 2)])
            else:
                res.append(res[i - 1] + 1)
        return res


print(Solution().countBits(1))
