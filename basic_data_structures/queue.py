# http://interactivepython.org/runestone/static/pythonds/BasicDS/WhatIsaQueue.html
# http://interactivepython.org/runestone/static/pythonds/BasicDS/TheQueueAbstractDataType.html
# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaQueueinPython.html
# http://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationHotPotato.html
# http://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationPrintingTasks.html

# What is a queue?

# An ordered collection of items.

# Addition of new items happens at one end (rear).

# Removal of existing elements occurs at other end (front).

# FIFO, first-in first-out


# Queue Abstract Data Type

# Queue()
#   creates a new empty queue. Needs no parameters and returns an empty queue

# enqueue(item)
#   adds a new item to the rear of a queue. Needs the item, returns nothing

# dequeue()
#   removes the front item from the queue. No parameters, returns the item.
#   Modifies the queue.

# isEmpty()
#   tests to see if the queue is empty. No parameters, returns a boolean.

# size()
#   returns the number of items in a queue. No parameters, returns an integer


# Implementing a Queue in Python

# Implementation of choice for ADT is a new class
# Queue operations as methods
# Utilize primitive collections (list in this case)
# List allows us to use insert for enqueue (O(n)) and pop for dequeue (O(1))

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Create a queue and call methods

q = Queue()

q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())


# Hot Potato simulation

def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()

    return sim_queue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))


# Printer simulation

class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60/self.page_rate

import random


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):

        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait {0:6.2f} sec {1:3d} tasks remaining."
          .format(average_wait, print_queue.size()))


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


print("--- Printer simulation ---")
for i in range(10):
    simulation(3600, 5)