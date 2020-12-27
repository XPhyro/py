#!/usr/bin/env python3


import re
import datetime as dt
import input_helper as ih


def getdate(msg):
    while True:
        s = re.sub("\s|[-/_|,.]", "", input(msg))

        l = len(s)
        if l != 4:
            if l != 8:
                print("Input could not be understood.")
                continue
            else:
                try:
                    year = int(s[0:4])
                    month = int(s[4:6])
                    day = int(s[6:8])

                    return dt.datetime(year, month, day)
                except:
                    print("You must enter a valid date.")
                    continue
        else:
            try:
                year = 2020
                month = int(s[0:2])
                day = int(s[0:4])

                return dt.datetime(year, month, day)
            except:
                print("You must enter a valid date.")
                continue


now = dt.datetime.now()
date = getdate("Enter date: ")

print(date - now)
