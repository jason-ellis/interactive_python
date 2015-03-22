# http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/Lists.html

# Indexing and assigning are O(1)

# Adding to a list:
# Append is O(1)
# Concatenate is O(k) where k is the size of the list being concatenated


# Methods of generating a list:

# for loop and concatenate
def test1():
    l = []
    for i in range(1000):
        l = l + [i]


# for loop and append
def test2():
    l = []
    for i in range(1000):
        l.append(i)


# list comprehension
def test3():
    l = [i for i in range(1000)]


# range function in constructor
def test4():
    l = list(range(1000))

# Run tests using timeit module
from timeit import Timer

print("--- Testing list generation ---")

t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ", t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "milliseconds")

# Conclusion:
# append was faster than concat
# list constructor was faster than list comprehension

"""
Big-O Efficiency of Python List Operators

index []            O(1)
index assignment    O(1)
append              O(1)
pop()               O(1)
pop(i)              O(n)
insert(i, item)     O(n)
del operator        O(n)
iteration           O(n)
contains (in)       O(n)
get slice [x:y]     O(k)
del slice           O(n)
get slice           O(n+k)
reverse             O(n)
concatenate         O(k)
sort                O(k)
multiply            O(nk)
"""

# Compare pop performance on end and front of list

print("--- Testing pop zero vs end ---")

pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
print("pop zero ", pop_zero.timeit(number=1000))

x = list(range(2000000))
print("pop end ", pop_end.timeit(number=1000))

# Conclusion:
# Popping from the end was much faster than popping zero


# Compare pop zero vs end against growing list to determine Big-O
print("--- Testing Big-O of pop zero and end ---")

pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

print("pop(0)   pop()")
for i in range(1000000, 100000001, 1000000):
    x = list(range(i))
    pt = pop_end.timeit(number=1000)
    x = list(range(i))
    pz = pop_zero.timeit(number=1000)
    print("{0:15.5f}, {1:15.5f}".format(pz, pt))

# Conclusion:
# pop end is O(1), the execution time stays flat as the list grows
# pop zero is O(n), the execution time grows linearly as the list grows