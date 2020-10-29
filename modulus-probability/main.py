#!/usr/bin/env python3


from time import time
import num_helper as nh


MAX = 1000000000

p = 0
t = 0

t0 = time()

for i in range(1, MAX + 1):
    for k in str(i):
        if k == "0" or k == "1":
            continue
        if i % int(k) == 0:
            p += 1
        t += 1

t1 = time()

print(f"p:\t{p}")
print(f"t:\t{t}")
print(f"p/t:\t{p / t}")
print(f"t0:\t{t0}")
print(f"t1:\t{t1}")
print(f"t1-t0:\t{t1 - t0}")
