# http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/WhatIsAlgorithmAnalysis.html


# Simple sum function
def sum_of_n(n):
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i

    return the_sum


# Terrible sum function
def foo(tom):
    fred = 0
    for bill in range(1,tom+1):
        barney = bill
        fred = fred + barney

    return fred

# Timed sum function
import time


def sum_of_n2(n):
    start = time.time()

    the_sum = 0
    for i in range(1,n+1):
        the_sum = the_sum + i

    end = time.time()

    return the_sum, end-start

for i in range(5):
    print("Sum is {0[0]} required {0[1]:10.7f} seconds"
          .format(sum_of_n2(10000)))

for i in range(5):
    print("Sum is {0[0]} required {0[1]:10.7f} seconds"
          .format(sum_of_n2(100000)))

for i in range(5):
    print("Sum is {0[0]} required {0[1]:10.7f} seconds"
          .format(sum_of_n2(1000000)))


# Closed equation without iterating
def sum_of_n3(n):
    start = time.time()

    return (n*(n+1))/2


def time_sum_of_n3(n):
    start = time.time()

    the_sum = sum_of_n3(n)

    end = time.time()

    return the_sum, end-start

print("Sum is {0[0]} required {0[1]:10.7f} seconds"
      .format(time_sum_of_n3(10000000000)))