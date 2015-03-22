# http://interactivepython.org/runestone/static/pythonds/BasicDS/WhatisaStack.html
# http://interactivepython.org/runestone/static/pythonds/BasicDS/TheStackAbstractDataType.html
# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html


# What is a stack?

# Sometimes called a "push-down stack"

# An ordered collection of items where the addition of new items and the removal
# of existing items always takes place at the same end: the "top."

# LIFO: Last-in first-out. Ordering is based on collection length

# Efficient for reversing a collection.


# Stack Abstract Data Type

# Stack()
#   creates a new empty stack. It needs no parameters and returns an empty stack

# push(item)
#   adds a new item to the top of a stack. Takes item, returns nothing

# pop()
#   removes the top item from stack. No parameters, returns the item.
#   Modifies stack

# peek()
#   returns top item from stack, doesn't remove it. no parameters, stack is
#   not modified

# isEmpty()
#   tests to see if the stack is empty. No parameters, returns boolean

# size()
#   returns the number of items in the stack. No parameters, returns integer


# Implementing a Stack in Python

# Implementation of choice for ADT is a new class
# Stack operations as methods
# Utilize primitive collections (list in this case)

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# Create stack and call methods
s = Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

# Implementation can also use the beginning of the list as the top of the stack
# This is inefficient in Python using a list and will change push and pop
# operations from O(1) to O(n)