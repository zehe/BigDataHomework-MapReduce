#!/usr/bin/python
import sys

current_trip_number = 1
current_taxi = None
total_days = 1
current_date = None

for line in sys.stdin:
    taxi, trip = line.strip().split("&", 1)
    pickup_date, trip_number = trip.strip().split("\t", 1)

    try:
        trip_number = int(trip_number)
    except ValueError:
        continue

    if taxi == current_taxi:
        current_trip_number += trip_number
        if pickup_date != current_date:
            total_days += 1
    else:
        if current_taxi:
            print("%s\t%d,%.2f" % (current_taxi, current_trip_number, float(current_trip_number / total_days)))
        current_taxi = taxi
        current_date = pickup_date
        current_trip_number = 1
        total_days = 1

print("%s\t%d,%.2f" % (current_taxi, current_trip_number, float(current_trip_number / total_days)))
