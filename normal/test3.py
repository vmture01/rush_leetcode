#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test3.py
# @Author: vmture
# @Date  : 2020/9/3
# @Desc  : 找出克隆二叉树中的相同节点

# https://leetcode-cn.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# 给你两棵二叉树，原始树 original 和克隆树 cloned，以及一个位于原始树 original 中的目标节点 target。
#
# 其中，克隆树 cloned 是原始树 original 的一个 副本 。
#
# 请找出在树 cloned 中，与 target 相同 的节点，并返回对该节点的引用（在 C/C++ 等有指针的语言中返回 节点指针，其他语言返回节点本身）。
#
#  
#
# 注意：
#
# 你 不能 对两棵二叉树，以及 target 节点进行更改。
# 只能 返回对克隆树 cloned 中已有的节点的引用。
# 进阶：如果树中允许出现值相同的节点，你将如何解答？
#
# 输入: tree = [7,4,3,null,null,6,19], target = 3
# 输出: 3
# 解释: 上图画出了树 original 和 cloned。target 节点在树 original 中，用绿色标记。答案是树 cloned 中的黄颜色的节点（其他示例类似）。
#
# 输入: tree = [7], target =  7
# 输出: 7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 递归比较的时候记录下来，然后返回

class Solution:
    def getTargetCopy(self, original, cloned, target):
        def clone_node(node):
            if not node:
                return None
            if node.val == target.val:
                self.res = node
            clone_node(node.left)
            clone_node(node.right)

        clone_node(cloned)
        return self.res
