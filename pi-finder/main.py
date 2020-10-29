#!/usr/bin/env python3

import sys
import datetime
import mmap


s = sys.argv[1:]

if len(s) == 0:
    print("No input was given, exiting.")
    sys.exit()

toOmmit = []
for i in s:
    try:
        if int(i) <= -1:
            raise ValueError()
    except ValueError:
        print(f"Omitting {i} as it is invalid.")
        toOmmit.append(i)

for i in toOmmit:
    s.remove(i)

with open("pi-billion.txt", "r") as f:
    pi = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    print(f"Initiated search on {datetime.datetime.now()}.")
    indices = [pi.find(i.encode("utf-8")) for i in s]
    print(f"Finished search on {datetime.datetime.now()}.")

for i, j in enumerate(indices):
    if j == -1:
        print(f"{s[i]} could not be found.")
    else:
        print(f"Index of {s[i]} is {j}.")
