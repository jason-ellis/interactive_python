# http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/Dictionaries.html

# get item and set item are O(1)

# contains is O(1)

# get, set, and contains can degenerate to O(n)

"""
Big-O Efficiency of Python Dictionary Operations

copy            O(n)
get item        O(1)
set item        O(n)
delete item     O(1)
contains (in)   O(1)
iteration       O(n)
"""

# Compare performance of "list in" and "dict in"
import timeit
import random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange({}) in x".format(i),
                     "from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("{0},{1:10.3f},{2:10.3f}".format(i, lst_time, d_time))

# Conclusion:
# "list in" is O(n), grows linearly as list grows
# "dict in" is O(1), remains constant as dict grows