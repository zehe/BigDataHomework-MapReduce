#!/usr/bin/python

import sys

for line in sys.stdin:
    carInfo,tripInfo = line.strip().split('\t',1)
    tripInfo = tripInfo.split(',')
    try:
        fare = float(tripInfo[-6])
    except ValueError:
        continue

    if fare <= 4 and fare >= 0:
        print "%s\t%d"%('0,4',1)
    elif fare <= 8 and fare >4:
        print "%s\t%d"%('4.01,8',1)
    elif fare <= 12 and fare >8:
        print "%s\t%d"%('8.01,12',1)
    elif fare <= 16 and fare > 12:
        print "%s\t%d"%('12.01,16',1)
    elif fare <= 20 and fare > 16:
        print "%s\t%d"%('16.01,20',1)
    elif fare <= 24 and fare > 20:
        print "%s\t%d"%('20.01,24',1)
    elif fare <= 28 and fare > 24:
        print "%s\t%d"%('24.01,28',1)
    elif fare <= 32 and fare > 28:
        print "%s\t%d"%('28.01,32',1)
    elif fare <= 36 and fare > 32:
        print "%s\t%d"%('32.01,36',1)
    elif fare <= 40 and fare > 36:
        print "%s\t%d"%('36.01,40',1)
    elif fare <= 44 and fare > 40:
        print "%s\t%d"%('40.01,44',1)
    elif fare <= 48 and fare > 44:
        print "%s\t%d"%('44.01,48',1)
    elif fare > 48:
        print "%s\t%d"%('48.01,infinite',1)
