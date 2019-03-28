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


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    while not s.is_empty():
        s.pop()
        s.pop()

