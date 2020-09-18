#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 快速排序.py
# @Author: vmture
# @Date  : 2020/9/15
# @Desc  : https://www.runoob.com/python3/python-quicksort.html

# arr = [10, 7, 8, 9, 1, 5]
#
#
# def d(arr, low, high):
#     base = arr[high]
#     j = low - 1
#     for i in range(low, high):
#         if arr[i] <= base:
#             j += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[j + 1], arr[high] = arr[high], arr[j + 1]
#     return j + 1
#
#
# def quickSort(arr, low, high):
#     pi = d(arr, low, high)
#     quickSort(arr, low, pi - 1)
#     quickSort(arr, pi + 1, high)
#     return arr
#
#
# print(quickSort(arr, 0, 4))
def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]

    for j in range(low, high):
        print(pivot)
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
        print(arr)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(arr)
    return (i + 1)


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print("pi%s" % pi)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 2, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
# print("排序后的数组:")
# for i in range(n):
#     print("%d" % arr[i]),
