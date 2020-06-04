from mpmath import *
from mpmath import mp
import time

while True:
    s = input("To how many decimal points should pi be calculated?\n> ")
    try:
        s = int(s)
    except:
        continue
    if s > 0:
        mp.dps = s
        break

print(f"Calculating pi to {mp.dps} digits.")

t0 = time.time()

p = str(pi())

t1 = time.time()

print('Calculation completed.\nWriting pi to file "pi".')

with open("pi", "w+") as f:
    for i in p:
        f.write(i)
    f.write("\n")
    f.close()

print('Writing pi completed.\nWriting pi to file "time".')

with open("time", "w+") as f:
    f.write(str(t0) + "\n" + str(t1) + "\n" + str(t1 - t0) + "\n")
    f.close()

print("Writing time completed.")

print("Exiting.")
