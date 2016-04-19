#!/usr/bin/python
import sys

for line in sys.stdin:
    key, value = line.strip().split('\t')
    value = value.replace('VALUE: ', '')
    fare_amount = value.split(',')[16]

    print ("%s&%d" % (fare_amount, 1))
