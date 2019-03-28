# /usr/bin/env python
# -*- coding:utf-8 -*-
import heapq


def find_small_k_sums(alist, k):
    max_heap = []
    if not alist or k < 0 or k > len(alist):
        return
    for ele in alist:
        ele = -ele
        if len(max_heap) < k:
            heapq.heappush(max_heap, ele)
        else:
            heapq.heappushpop(max_heap, ele)
    return list(map(lambda x: -x, max_heap))


if __name__ == "__main__":
    alist = [0, 1, 4, 3, 5, 9, 2, 8, 6]
    min_k = find_small_k_sums(alist, 2)
    print(min_k)