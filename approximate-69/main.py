#!/usr/bin/env python3


from math import sin, cos, tan, sqrt
from time import time


s = 0
c = 0.2235
dc = 0.00001
m = 69.696969696969
dm = 0.00000000000002
v = 1

t0 = time()

while not m <= s <= m + dm:
    s = 0
    for i in range(10):
        s += i + sin(i) + cos(i) + tan(i) + sqrt(i) + c

    if s < m:
        if v > 0:
            old_dc = dc
            dc /= 10
            if old_dc == dc:
                break
        v = -1
        c += dc
    else:
        if v < 0:
            old_dc = dc
            dc /= 10
            if old_dc == dc:
                break
        v = 1
        c -= dc

t1 = time()

w = f"""Sum:\t{s}
Offset:\t{c}
Time:\t{t1 - t0}"""

print(w)

with open("result", "w+") as f:
    f.write(f"{w}\n")
