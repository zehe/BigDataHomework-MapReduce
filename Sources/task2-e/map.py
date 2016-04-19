#!/usr/bin/python
import sys
from datetime import datetime

for line in sys.stdin:

    key, value = line.strip().split('\t')
    key = key.replace('KEY: ', '')
    value = value.replace('VALUE: ', '')

    medallion = key.split(',')[0]
    pickup_datetime = key.split(',')[3]

    pickup_date = datetime.strptime(pickup_datetime, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

    print ("%s&%s\t%d" % (medallion, pickup_date, 1))
