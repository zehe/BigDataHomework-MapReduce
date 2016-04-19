#!/usr/bin/python
import sys

for line in sys.stdin:

    key, value = line.strip().split('\t')
    keys = key.replace('KEY: ', '').split(',')

    medallion = keys[0]
    license = keys[1]

    print ("%s\t%s" % (license, medallion))