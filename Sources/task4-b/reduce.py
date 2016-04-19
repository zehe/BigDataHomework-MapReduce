#!/usr/bin/python

import sys
import operator

current_agent = None
current_revenue = 0
count = {'None':0}
top = 8

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    agent, revenue = line.strip().split("\t", 1)

    try:
        revenue = float(revenue)
    except ValueError:
        continue

    if agent == current_agent:
        current_revenue += revenue

    else:
        if current_agent:
            # output goes to STDOUT (stream data that the program writes)
            count[current_agent] = current_revenue
        current_agent = agent
        current_revenue = revenue
count[current_agent] = current_revenue

for i in range(top):
    topAgent = max(count.iteritems(), key=operator.itemgetter(1))[0]
    print "%s\t%.2f"%(topAgent, count[topAgent])
    count[topAgent] = 0
