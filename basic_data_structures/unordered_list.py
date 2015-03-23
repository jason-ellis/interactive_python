# http://interactivepython.org/runestone/static/pythonds/BasicDS/Lists.html
# http://interactivepython.org/runestone/static/pythonds/BasicDS/TheUnorderedListAbstractDataType.html
# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html


# Implemented in Python's list data structure
# Each item holds a relative position with respect to the others.
# Cannot contain duplicate items


# The Unordered List Abstract Data Type

# List()
#   creates a new empty list. No parameters, returns an empty list

# add(item)
#   adds a new item to the list. Needs the item, returns nothing.
#   assumes the item is not already in the list

# remove(item)
#   removes the items from the list. Needs the item, modifies the list
#   assumes the item is present in the list.

# search(item)
#   searches for the item in the list. Needs the item, returns boolean

# is_empty()
#   tests whether the list is empty. Needs no parameters, returns boolean

# size()
#   returns the number of items in the list. No parameters, returns integer

# append(item)
#   adds a new item to the end of the list. Needs item and returns nothing.
#   assume the item is not already in the list

# index(item)
#   returns the position of item in the list. Needs the item, returns index
#   assume the item is in the list

# insert(pos, item)
#   adds a new item to the list at position pos. Needs item, returns nothing.
#   assume the item is not already in the list and there are enough existing
#   items to have position pos.

# pop()
#   removes and returns the last item in the list. Needs nothing, returns item.
#   assume the list has at least one item

# pop(pos)
#   removes and returns the item in position pos. It needs the position and
#   returns the item. Assume the item is in the list.


# Implementing an Unordered List: Linked Lists

# Implementation of choice for ADT is a new class
# Linked List consists of a Head that points to first item (node) in the list
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


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

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

    def append(self, item):
        current = self.head
        previous = None
        while current != None:
            previous = current
            current = current.get_next()

        temp = Node(item)
        previous.set_next(temp)

    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        else:
            current = self.head
            previous = None
            count = 0
            while count != pos:
                count = count + 1
                previous = current
                current = current.get_next()

            temp = Node(item)
            previous.set_next(temp)
            temp.set_next(current.get_next())

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
            while current != None:
                count = count + 1
                previous = current
                current = current.get_next()
            previous.set_next(None)
            return previous.get_data()
        elif pos == 0:
            self.head = current.get_next()
        else:
            while count != pos:
                count = count + 1
                previous = current
                current = current.get_next()

            previous.set_next(current.get_next())
        return current.get_data()

# Create linked list and call methods
my_list = UnorderedList()

print("List is empty?", my_list.is_empty())

my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

print("List is empty?", my_list.is_empty())
print("List size:", my_list.size())
print("Search for 17:", my_list.search(17), my_list.index(17))
print("Remove 17")
my_list.remove(17)
print("Search for 17:", my_list.search(17))
print("Append 12")
my_list.append(12)
print("Search for 12:", my_list.search(12), my_list.index(12))
my_list.insert(0, 14)
print("Insert 14 at 0:", my_list.search(14), my_list.index(14))
my_list.insert(1, 15)
print("Insert 15 at 1:", my_list.search(15), my_list.index(15))
print("Popping last (12):", my_list.pop())
print("Popping first (14)", my_list.pop(0))