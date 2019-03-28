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


def infixToPostfix(infixex):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    prec[')'] = 1
    tokenStack = Stack()
    opretorList = infixex.split()
    res = []
    print('oeretorList:', opretorList)
    for i in opretorList:
        print('i:', i)
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or i in '0123456789':
            res.append(i)
        elif i == '(':
            tokenStack.push(i)
        elif i == ')':
            token = tokenStack.pop()
            if token != '(':
                res.append(token)
                tokenStack.pop()
        else:
            while not tokenStack.is_empty() and prec[tokenStack.peek()] > prec[i]:
                res.append(tokenStack.pop())
            tokenStack.push(i)

    while not tokenStack.is_empty():
        res.append(tokenStack.pop())

    return ' '.join(res)

print(infixToPostfix('A * B + C * D'))

