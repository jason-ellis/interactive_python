# http://interactivepython.org/runestone/static/pythonds/BasicDS/WhatIsaDeque.html
# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaDequeinPython.html
# http://interactivepython.org/runestone/static/pythonds/BasicDS/PalindromeChecker.html


# What is a Deque?

# Also known as a double-ended queue.
# An ordered collection of items similar to the queue.
# Two ends, a front and a rear. Items remain positioned in the collection
# Items can be added to and removed from either end
# Provides all capabilities of stacks and queues in a single data structure
# Does not force LIFO or FIFO


# Deque Abstract Data Type

# Deque()
#   Creates a new empty deque. No parameters, returns an empty deque.

# add_front(item)
#   adds a new item to the front of the deque. Needs the item, returns nothing

# add_rear(item)
#   adds a new items to the rear of the deque. Needs the item, returns nothing

# remove_front()
#   removes the front item from the deque. No parameters, returns the item.
#   The deque is modified

# remove_rear()
#   removes the rear item from the deque. No parameters, returns the item.
#   The deque is modified

# is_empty()
#   test whether the deque is empty. No parameters, returns a boolean

# size()
#   returns the number of items in the deque. No parameters, returns an integer


# Implementing a Deque in Python

# Implementation of choice for ADT is a new class
# Deque operations as methods
# Utilize primitive collections (list in this case)
# Assume the rear of the deque is at position 0

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

# Create the deque and call methods
d = Deque()

print(d.is_empty())
d.add_rear(4)
d.add_rear('dog')
d.add_front('cat')
d.add_front(True)
print(d.size())
print(d.is_empty())
d.add_rear(8.4)
print(d.remove_rear())
print(d.remove_front())

# Adding and removing items from the front is O(1)
# Adding and removing from the rear is O(n)


# Palindrome checker

def pal_checker(a_string):
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_rear(ch)

    still_equal = True

    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            still_equal = False

    return still_equal

print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))
