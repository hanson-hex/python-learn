# /usr/bin/env python
# -*- coding:utf-8 -*-


# 快速排序
def partition(alist, start, end):
    if end <= start:
        return
    base = alist[start]
    while start < end:
        while start < end and alist[end] >= base:
            end -= 1
        alist[start] = alist[end]
        while start < end and alist[start] <= base:
            start += 1
        alist[end] = alist[start]
    alist[start] = base
    return start


def find_small_k_sums(alist, k):
    if not alist or k < 0 or k > len(alist):
        return
    start = 0
    end = len(alist) - 1
    index = partition(alist, start, end)
    while index != k:
        if index > k:
            index = partition(alist, start, index - 1)
        elif index < k:
            index = partition(alist, index + 1, end)
    return alist[:k]


if __name__ == "__main__":
    alist = [0, 1, 4, 3, 5, 9, 2, 8, 6]
    min_k = find_small_k_sums(alist, 2)
    print(min_k)