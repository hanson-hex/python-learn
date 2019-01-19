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


def getPostfixValue(postfixex):
    postfixStack = Stack()
    postfixexList = postfixex.split()

    for i in postfixexList:
        if i in '0123456789':
            postfixStack.push(int(i))
        else:
            num1 = postfixStack.pop()
            num2 = postfixStack.pop()
            res = doMach(i, num1, num2)
            postfixStack.push(res)

    return postfixStack.pop()


def doMach(token, num1, num2):
    if token == '*':
        return num1 * num2
    elif token == '/':
        return num1 / num2
    elif token == '+':
        return num1 + num2
    elif token == '-':
        return num1 - num2



print(getPostfixValue('7 8 + 6 *'))