# /usr/bin/env python
# -*- coding:utf-8 -*-


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, nxt):
        self.next = nxt


class OrderList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current and not found and not stop:
            if current.get_data() == item:
                found = True
            elif current.get_data() > item:
                stop = True
            else:
                current = current.get_next()
        return found

    def add(self, item):
        current = self.head
        pre = None
        stop = False
        while current and not stop:
            if current.get_data() <= item:
                pre = current
                current = current.get_next()
            else:
                stop = True

        temp = Node(item)
        if not pre:
            temp.set_next(current)
            self.head = temp
        else:

            temp.set_next(current)
            pre.set_next(temp)


