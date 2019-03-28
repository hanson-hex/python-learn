# /usr/bin/env python
# -*- coding:utf-8 -*-

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]


def coverter(num, base):
    digits = '0123456789ABCDEF'

    s = Stack()
    while num > 0:
        res = num % base
        num = num // base
        print('res: ', res)
        s.push(res)
    str = ''
    while not s.is_empty():
        str += digits[s.pop()]
    return str


if __name__ == '__main__':
    res = coverter(34, 16)
    print('res:', res)
