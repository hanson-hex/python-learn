"""
问题描述

　　给定n个正整数，找出它们中出现次数最多的数。如果这样的数有多个，请输出其中最小的一个。

输入格式

　　输入的第一行只有一个正整数n(1 ≤ n ≤ 1000)，表示数字的个数。
　　输入的第二行有n个整数s1, s2, …, sn (1 ≤ si ≤ 10000, 1 ≤ i ≤ n)。相邻的数用空格分隔。

输出格式

　　输出这n个次数中出现次数最多的数。如果这样的数有多个，输出其中最小的一个。

样例输入

6
10 1 10 20 30 20

样例输出

10
---------------------
"""

if __name__ == '__main__':
    n = eval(input())
    exam_list = list(map(int, input().split()))
    # tem_list = []
    # max_num_item = exam_list[0]
    # for i in range(n):
    #     if exam_list[i] not in tem_list:
    #         tem_list.append(exam_list[i])
    #         if exam_list.count(exam_list[i]) > exam_list.count(max_num_item):
    #             max_num_item = exam_list[i]
    #     else:
    #         continue
    b = list(set(exam_list))
    b.sort()
    s = dict(zip(b, map(exam_list.count, b)))
    print('s=', s)
    print(max(s, key=s.get))
    print(max(s.values()))

