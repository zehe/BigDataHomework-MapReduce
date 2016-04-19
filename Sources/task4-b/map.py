#!/usr/bin/python

import sys
import csv
import StringIO

for line in sys.stdin:
    csv_file = StringIO.StringIO(line)
    csv_reader = csv.reader(csv_file)
    for item in csv_reader:
        readLine = item
    agent = readLine[-6]
    try:
        fareAmount = float(readLine[14])
        surcharge = float(readLine[15])
        tip = float(readLine[17])
    except ValueError:
        continue
    revenue = fareAmount + surcharge + tip
    print "%s\t%.2f"%(agent,revenue)
