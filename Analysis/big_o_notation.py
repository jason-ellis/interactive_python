# http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/BigONotation.html
"""
a = 5
b = 6
c = 10
for i in range(n):
    for j in range(n):
        x = i * i
        y = j * j
        z = i * j
for k in range(n):
    w = a*k + 45
    v = b*b
d = 33

The number of assignment operations is the sum of 4 terms.

1st term = Constant 3. Assignment of a, b, c.
2nd term = 3n^2. 3 statements performed n^2 times (x, y, z nested for i...for j)
3rd term = 2n. w, v assigned n number of times.
4th term = Constant 1. Assignment of d.

T(n) = 3 + 3n^2 + 2n + 1 = 3n^2 + 2n + 4
n^2 is the dominant portion of the equation, so algorithm is O(n^2)
"""
