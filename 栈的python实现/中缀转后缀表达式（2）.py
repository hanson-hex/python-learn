# /usr/bin/env python
# -*- coding:utf-8 -*-
import re

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
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['−'] = 2
    prec['('] = 1
    prec[')'] = 1
    tokenStack = Stack()
    opretorList = re.split(r'([^\d])', infixex)
    res = []
    print('oeretorList:', opretorList)
    for i in opretorList:
        if i.isdigit():
            res.append(i)
            print('res:', res)
        elif i == '(':
            tokenStack.push(i)
        elif i == ')':
            token = tokenStack.pop()
            if token != '(':
                res.append(token)
                tokenStack.pop()
        elif i:
            print('i', i)
            print(type(i))
            if not tokenStack.is_empty():
                print('tokenStack顶前', tokenStack.peek())
                print('prec[tokenStack.peek()]', prec[tokenStack.peek()])
                print('prec[i]', prec[i])
            while not tokenStack.is_empty() and prec[tokenStack.peek()] > prec[i]:
                print('是否载入：', tokenStack.peek())
                res.append(tokenStack.pop())
            tokenStack.push(i)
            print('tokenStack顶后', tokenStack.peek())

    while not tokenStack.is_empty():
        res.append(tokenStack.pop())

    return ' '.join(res)

# print(infixToPostfix('45*12+14*16'))
# print(infixToPostfix('10+3*5/(16−4)'))
print(infixToPostfix('5*3^(4−2)'))
