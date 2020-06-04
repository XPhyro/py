#!/usr/bin/python


import math
from math import *
import input_helper as ih


def integrate(func, low, high, step):
    if low < high:
        old_low = low
        low = high
        high = old_low

    A = (func(low) + func(high)) / 2.0
    x = low + step

    while x < high:
        A += func(x)
        x += step
    return A * step


def custom0(x):
    return sin(cos(tan(x)))


lowerBoundary = ih.get_float("Enter the lower boundary:")
upperBoundary = ih.get_float("Enter the upper boundary:")
stepCount = ih.get_pint(
    "Enter a positive integer to be used as step count in the calculation of the integral:"
)

fnname = ""
fn = None

while not (isinstance(fn, type(math.log)) or isinstance(fn, type(integrate))):
    fnname = input("Enter the function:\n> ")
    try:
        fn = eval(fnname)
    except:
        continue

area = integrate(
    fn, lowerBoundary, upperBoundary, (lowerBoundary + upperBoundary) / stepCount
)

print(
    f"The integral of {fnname} from {lowerBoundary} to {upperBoundary} with {stepCount} steps is\nA = {area}"
)
