#!/usr/bin/env python3


from input_helper import get_nonnint
from numpy import base_repr


n = get_nonnint("Enter n:")
b = get_nonnint("Enter b:") + 1

for i in range(b ** n):
    s = base_repr(i, b)
    print("0" * (n - len(s)) + s)
