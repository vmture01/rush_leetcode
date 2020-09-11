#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test12.py
# @Author: vmture
# @Date  : 2020/9/11
# @Desc  : 组合总和

# https://leetcode-cn.com/problems/combination-sum/

# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1：
#
# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#   [7],
#   [2,2,3]
# ]
# 示例 2：
#
# 输入：candidates = [2,3,5], target = 8,
# 所求解集为：
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#  
#
# 提示：
#
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# candidate 中的每个元素都是独一无二的。
# 1 <= target <= 500


class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        res = []
        path = []
        length = len(candidates)

        def h(begin, path1, target1):
            if target1 == 0:
                res.append(path1)
            for i in range(begin, length):
                if target1 < 0:
                    break
                h(i, path1 + [candidates[i]], target1 - candidates[i])

        h(0, path, target)
        return res


print(Solution().combinationSum([2, 3, 5], 8))
