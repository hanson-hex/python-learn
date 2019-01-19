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


def par_checker(symbol_string):
    balance = True
    s = Stack()
    index = 0
    while index < len(symbol_string) and balance:
        symbol = symbol_string[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if not s.is_empty():
                top = s.pop()
                if not matched(top, symbol):
                    balance = False
            else:
                balance = False
        index = index + 1

    if balance and s.is_empty():
        return True
    else:
        return False


def matched(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)


if __name__ == '__main__':
    print(par_checker('((()))[](())'))