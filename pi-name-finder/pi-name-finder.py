#!/usr/bin/env python3

import datetime

with open("pi-billion.txt", "r") as f:
    print(f"Initiated search on {datetime.datetime.now()}.")
    pi = f.read()
    string = input()
    i = pi.find(str(int(string, 36)))
    print(f"Completed search on {datetime.datetime.now()}.")
    print(
        f'Index of "{string}" (in base 36) in pi (not including the 3. part) is {i - 2}.'
    )
    f.close()
