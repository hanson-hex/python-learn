# /usr/bin/env python
# -*- coding:utf-8 -*-

# 快速排序
def partition(alist, start, end):
    if end <= start:
        return
    base = alist[start]
    index1, index2 = start, end
    while start < end:
        while start < end and alist[end] >= base:
            end -= 1
        alist[start] = alist[end]
        while start < end and alist[start] <= base:
            start += 1
        alist[end] = alist[start]
    alist[start] = base
    partition(alist, index1, start - 1)
    partition(alist, start + 1, index2)


def find_small_k_sums(alist, k):
    if not alist or k < 0 or k > len(alist):
        return
    start = 0
    end = len(alist) - 1
    partition(alist, start, end)
    return alist[:k]


if __name__ == "__main__":
    alist = [1, 3, 4, 3, 5, 9, 2, 8, 0]
    min_k = find_small_k_sums(alist, 7)
    print(min_k)


