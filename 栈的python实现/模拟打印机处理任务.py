# /usr/bin/env python
# -*- coding:utf-8 -*-
import queue
import random


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


class Printer:
    def __init__(self, ppm):
        # 每分钟处理的纸张数目
        self.ppm = ppm
        self.currentTask = None
        self.remainTime = 0

    def is_busy(self):
        if self.currentTask:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.currentTask = new_task
        self.remainTime = new_task.get_pages() * 60 / self.ppm

    def click(self):
        if self.currentTask:
            self.remainTime -= 1
            if self.remainTime <= 0:
                self.currentTask = None


class Task:
    def __init__(self, second):
        self.start_time = second
        self.pages = random.randrange(1, 21)

    def wait_time(self, stop_time):
        return stop_time - self.start_time

    def get_pages(self):
        return self.pages

    def get_stamp(self):
        return self.start_time


def simulation(nums_seconds, pages_per_minute):
    work_printer = Printer(pages_per_minute)
    print_queue = Queue()
    await_time = []
    for second in range(nums_seconds):
        if new_work_task():
            new_task = Task(second)
            print_queue.enqueue(new_task)
            if not work_printer.is_busy() and not print_queue.is_empty():
                # print('现在可以处理任务le')
                item_task = print_queue.dequeue()
                # print('second:', second)
                await_time.append(item_task.wait_time(second))
                # print('await_time:', await_time)
                work_printer.start_next(new_task)
        work_printer.click()

    avavage_wait = sum(await_time) / len(await_time)
    print('平均每次任务需要的时间为：{}秒, 还剩下{}个任务未处理'.format(avavage_wait, print_queue.size()))


def new_work_task():
    num = random.randrange(1, 181)
    # return num == 180
    return num == 180


for i in range(10):
    simulation(3600, 5)
