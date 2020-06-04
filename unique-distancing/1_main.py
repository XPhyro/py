#!/usr/bin/env python3


from math import sqrt
import matrix_helper as mh


def iscombvalid(s):
    ds = []

    for i, j in enumerate(s):
        s[i] = (j // 6, j % 6)

    for i in s:
        for j in s:
            d = sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2)
            if d in ds:
                return False
            ds.append(d)


solutions = []

for s1 in range(36):
    for s2 in range(36):
        if s1 == s2:
            continue
        print(s1, s2)
        for s3 in range(36):
            if s1 == s3 or s2 == s3:
                continue
            for s4 in range(36):
                if s1 == s4 or s2 == s4 or s3 == s4:
                    continue
                for s5 in range(36):
                    if s1 == s5 or s2 == s5 or s3 == s5 or s4 == s5:
                        continue
                    for s6 in range(36):
                        if s1 == s6 or s2 == s6 or s3 == s6 or s4 == s6 or s5 == s6:
                            continue
                        s = [s1, s2, s3, s4, s5, s6]
                        if iscombvalid(s):
                            solutions.append(s)
                            print(f"Solution: {s}")

print(f"\n\nSolutions:\n{solutions}")
