#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test15.py
# @Author: vmture
# @Date  : 2020/9/10
# @Desc  : 翻转二叉树

# https://leetcode-cn.com/problems/invert-binary-tree/

# 翻转一棵二叉树。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
