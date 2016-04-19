#!/usr/bin/python
import sys

number = 0
current_passenger = None

for line in sys.stdin:

    passenger, count = line.strip().split("&", 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if passenger == current_passenger:
        number += count
    else:
        if current_passenger:
            print("%s\t%d" % (current_passenger, number))
        current_passenger = passenger
        number = count

print("%s\t%d" % (current_passenger, number))

