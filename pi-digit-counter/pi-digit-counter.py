#!/usr/bin/env python3


import os, time


maxN = os.stat("pi-billion.txt").st_size
with open("pi-billion.txt") as f:
    counts = [0 for i in range(10)]

    blockSize = 16384
    n = 2

    print("Processing pi file.")

    t0 = time.time()

    data = f.read(n)

    if "." in data:
        data = f.read(blockSize)

    while data:
        print(f"{n}B / {maxN}B")
        for i in data:
            j = int(i)
            counts[j] += 1

        data = f.read(blockSize)
        n += blockSize
        print("\x1b[1A\x1b[2K", end="")

    t1 = time.time()

print("Processing complete, here are the results:\n")

totalCount = sum(counts)
s = f"Total count\t\t{totalCount}\n"
for i in range(len(counts)):
    s += f"Count of {i}\t\t{counts[i]}\n"
s += f"\nTotal probability\t{1.0}"
for i in range(len(counts)):
    s += f"\nProbability of {i}\t{counts[i] / totalCount}"
s += f"\n\nBlock size\t\t{blockSize}\n"
s += f"Time taken\t\t{t1 - t0}s\n"

print(s, end="")

with open("stats", "w+") as f:
    print('\nWriting the results to file "stats".')
    f.write(s)
print("Writing complete.")
