#!/usr/bin/python
import sys

num = 0

for line in sys.stdin:

    total, count = line.strip().split("&", 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if float(total) <= 10:
        num += count


print("%d" % num)

