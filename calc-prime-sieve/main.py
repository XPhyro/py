#!/usr/bin/env python3


from input_helper import get_int_rng as get_limit


domain = [i for i in range(2, get_limit("Enter an integer greater than or equal to 2 to compute prime numbers until.", low=2) + 1)]

i = -1
while (i := i + 1) < len(domain):
    prime = domain[i]
    for elem in domain:
        if elem % prime == 0 and prime != elem:
            domain.remove(elem)

print(domain)
