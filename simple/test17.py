#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test17.py
# @Author: vmture
# @Date  : 2020/9/11
# @Desc  : 反转链表

# https://leetcode-cn.com/problems/reverse-linked-list/

# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def h(head1, num):
            if not head1.next or num == 5:
                return
            head1.val, head1.next.val = head1.next.val, head1.val
            h(head1.next, num + 1)

        for i in range(5):
            h(head, i)
        return head


class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        res = []

        def h(head1, n):
            if not head1.next:
                return
            res.insert(0, head1)
            for i in range(len(res) - n):
                res[i].val, res[i].next.val = res[i].next.val, res[i].val
            h(head1.next, n + 1)

        h(head, 0)
        return head


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        res = []

        def h(head1):
            if not head1:
                return
            res.insert(0, head1.val)
            h(head1.next)

        h(head)

        def h1(head2, n):
            if not head2:
                return
            head2.val = res[n]
            h1(head2.next, n + 1)

        h1(head, 0)
        return head
