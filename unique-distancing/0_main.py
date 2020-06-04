#!/usr/bin/env python3


from math import sqrt
import matrix_helper as mh


HEIGHT = 6
WIDTH = 6
QTY = 6


def is_distinct(s, distances):
    for j in indices:
        for k in indices:
            d = sqrt((j[0] - k[0]) ** 2 + (j[1] - k[1]) ** 2)
            if d in distances:
                return False
            distances.append(d)

    return True


mat = mh.init_mat(HEIGHT, WIDTH, False)
solutions = []

for i in range(2 ** (HEIGHT * WIDTH)):
    s = "{0:036b}".format(i)

    indices = [(j // WIDTH, j % WIDTH) for j, x in enumerate(s) if x == "1"]

    if len(indices) != QTY:
        continue

    distances = []

    if is_distinct(s, distances):
        solutions += s
        print(f"Solution: {s} where {i}")

    if not i % 100000:
        print(f"#{i}")

print("\n\nSolutions:")
print(solutions)
