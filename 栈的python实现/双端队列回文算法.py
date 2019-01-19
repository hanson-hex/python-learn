# /usr/bin/env python
# -*- coding:utf-8 -*-


class Dequeue:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop()

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def empty(self):
        return self.items == []


def palindrome_checker(string):
    new_dequeue = Dequeue()
    for i in string:
        new_dequeue.add_rear(i)

    is_palindrome = True
    if new_dequeue.size() > 1 and is_palindrome:
        front_item = new_dequeue.remove_front()
        rear_item = new_dequeue.remove_rear()
        if front_item != rear_item:
            is_palindrome = False

    return is_palindrome


print(palindrome_checker('dfdasghfdsjgfds'))
print(palindrome_checker('dsfdgdfsd'))
