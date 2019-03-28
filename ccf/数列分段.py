"""
问题描述

　　给定一个整数数列，数列中连续相同的最长整数序列算成一段，问数列中共有多少段？

输入格式

　　输入的第一行包含一个整数n，表示数列中整数的个数。
　　第二行包含n个整数a1, a2, …, an，表示给定的数列，相邻的整数之间用一个空格分隔。

输出格式

　　输出一个整数，表示给定的数列有多个段。

样例输入

8
8 8 8 0 12 12 8 0

样例输出

5

样例说明

　　8 8 8是第一段，0是第二段，12 12是第三段，倒数第二个整数8是第四段，最后一个0是第五段。

评测用例规模与约定

　　1 ≤ n ≤ 1000，0 ≤ ai ≤ 1000。
---------------------
"""
import time

if __name__ == '__main__':
    # n = eval(input())
    # exam_list = list(map(int, input().split()))
    # count = 1
    # last = exam_list[0]
    # for i in exam_list:
    #     if last != i:
    #         count += 1
    #     last = i
    # print(count)
    start = time.clock()
    sum = 0
    for i in range(100000):
        sum += i
    print(sum)
    end = time.clock()
    print('runing time: %s ms', (end - start)*1000)

