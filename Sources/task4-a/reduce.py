#!/usr/bin/python

import sys

current_carType = None
current_count = 0
current_revenue = 0
current_tipPercentage = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    carType, info = line.strip().split("\t", 1)
    revenue, tipPercentage = info.strip().split(',')

    try:
        revenue = float(revenue)
        tipPercentage = float(tipPercentage)
    except ValueError:
        continue

    if carType == current_carType:
        current_count += 1
        current_revenue += revenue
        if revenue != 0:
            current_tipPercentage += tipPercentage

    else:
        if current_carType:
            # output goes to STDOUT (stream data that the program writes)
            print "%s\t%d,%.2f,%.2f" %( current_carType, current_count, current_revenue, current_tipPercentage/current_count)
        current_carType = carType
        current_revenue = revenue
        if revenue != 0:
            current_tipPercentage = tipPercentage
        else:
            current_tipPercentage = 0
        current_count = 1
print "%s\t%d,%.2f,%.2f" %( current_carType, current_count, current_revenue, current_tipPercentage/current_count)
