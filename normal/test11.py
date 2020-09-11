#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test11.py
# @Author: vmture
# @Date  : 2020/9/11
# @Desc  : 94. 二叉树的中序遍历

# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

# 给定一个二叉树，返回它的中序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def inorderTraversal(self, root: TreeNode) -> list:
        # 设置颜色,白新的，灰出现过的
        white, gray = 0, 1
        res = []
        # 把第一个中间节点放进去，设为新的
        stack = [(white, root)]
        while stack:
            # 取出最先进去的节点
            color, node = stack.pop()
            # 如果节点不存在，跳过
            if not node:
                continue
            # 如果是新节点，把左右两个叶子节点置为新放进去，中间节点置为灰
            if not color:
                stack.append((white, node.right))
                stack.append((gray, node))
                stack.append((white, node.left))
            # 如果是旧节点 放进去res
            else:
                res.append(node.val)
        return res
