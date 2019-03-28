"""
问题描述

　　给定n个整数表示一个商店连续n天的销售量。如果某天之前销售量在增长，而后一天销售量减少，则称这一天为折点，反过来如果之前销售量减少而后一天销售量增长，也称这一天为折点。其他的天都不是折点。如下图中，第3天和第6天是折点。

　　给定n个整数a1, a2, …, an表示销售量，请计算出这些天总共有多少个折点。
　　为了减少歧义，我们给定的数据保证：在这n天中相邻两天的销售量总是不同的，即ai-1≠ai。注意，如果两天不相邻，销售量可能相同。

输入格式

　　输入的第一行包含一个整数n。
　　第二行包含n个整数，用空格分隔，分别表示a1, a2, …, an。

输出格式

　　输出一个整数，表示折点出现的数量。

样例输入

7
5 4 1 2 3 6 4

样例输出

2

评测用例规模与约定

　　所有评测用例满足：1 ≤ n ≤ 1000，每天的销售量是不超过10000的非负整数
---------------------
"""

def break_num(n, e_list):
    temp_list = []
    for index, item in enumerate(e_list):
        if index == 0 or index == len(e_list) - 1:
            continue
        if item < e_list[index - 1] and item < e_list[index + 1]:
            temp_list.append(item)
        elif item > e_list[index - 1] and item > e_list[index + 1]:
            temp_list.append(item)
    return len(temp_list)


if __name__ == '__main__':
    n = eval(input())
    exam_list = list(map(int, input().split()))
    print(break_num(n, exam_list))