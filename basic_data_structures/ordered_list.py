# http://interactivepython.org/runestone/static/pythonds/BasicDS/TheOrderedListAbstractDataType.html
# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganOrderedList.html


# Items hold relative position based upon underlying characteristic of item
# Ordering is typically either ascending or descending
# Assume list items have a meaningful comparison operation already defined


# The Ordered List Abstract Data Type

# OrderedList()
#   creates new empty ordered list. No parameters, returns empty list

# add(item)
#   adds a new item and preserves order. Needs item, returns nothing.
#   assumes the item is not already in the list

# remove(item)
#   removes item from list. Needs item, modifies the list.
#   assumes the item is in the list.

# search(item)
#   searches for item in list. Needs item and returns boolean

# is_empty()
#   tests whether the list is empty. Needs no parameters, returns boolean

# size()
#   returns the number of items in list. No parameters, returns integer

# index(item)
#   returns position of item in the list. Needs the item, returns index.
#   assumes the item is in the list.

# pop()
#   removes and returns the last item in the list. Needs nothing, returns item.
#   assumes the list has at least one item.

# pop(pos)
#   removes and returns the item at position pos. Needs position and
#   returns the item. Assumes the item is in the list.


# Implementing an Ordered List

# Implementation of choice for ADT is a new class
# Similar to unordered list, head and pointers to items
# Each item (node) contains data and reference to next item
# Implementation uses assumptions stated above regarding item existence

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def index(self, item):
        current = self.head
        count = 0
        while current.get_data() != item:
            count = count + 1
            current = current.get_next()

        return count

    def pop(self, pos=None):
        current = self.head
        previous = None
        count = 0

        if pos == None:
            while current.get_next() != None:
                count = count + 1
                previous = current
                current = current.get_next()
            previous.set_next(None)
            return current.get_data()
        elif pos == 0:
            self.head = current.get_next()
        else:
            while count != pos:
                count = count + 1
                previous = current
                current = current.get_next()

            previous.set_next(current.get_next())
        return current.get_data()


# Create list and call methods
my_list = OrderedList()

my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

print(my_list.size())
print(my_list.search(93))
print(my_list.search(100))
print(my_list.index(31))

print(my_list.pop())
print(my_list.size())
print(my_list.search(93))