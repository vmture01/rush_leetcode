#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test13.py
# @Author: vmture
# @Date  : 2020/9/11
# @Desc  : 二叉树展开为链表

# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/

# 给定一个二叉树，原地将它展开为一个单链表。

# 例如，给定二叉树
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# 将其展开为：
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []

        def h(node):
            if not node:
                return
            res.append(node.val)
            h(node.left)
            h(node.right)

        h(root)

        def h1(node1, n):
            node1.left = None
            node1.val = res[n]
            h1(node1.right, n + 1)

        h1(root, 0)

class Solution:
    def flatten(self, root):
        while root:
            if root.left:   #左子树存在的话才进行操作
                sub_left = root.left
                while sub_left.right:   #左子树的右子树找到最深
                    sub_left = sub_left.right
                sub_left.right = root.right #将root的右子树挂到左子树的右子树的最深
                root.right = root.left      #将root的左子树挂到右子树
                root.left = None            #将root左子树清空
            root = root.right
