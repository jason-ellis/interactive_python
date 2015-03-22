# http://interactivepython.org/runestone/static/pythonds/BasicDS/WhatIsaQueue.html
# http://interactivepython.org/runestone/static/pythonds/BasicDS/TheQueueAbstractDataType.html


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