#!/usr/bin/python
import sys

current_key = None
current_tag = None
current_values = []

for line in sys.stdin:
    key_tag, values = line.strip().split('&', 1)
    key, tag = key_tag.strip().split('\t', 1)
    if current_key == key:
        if current_tag != tag:
            if current_tag == "trip":
                value1 = values
                for current_value in current_values:
                    value2 = current_value
                    print '%s\t%s' % (current_key, value2 + "," + value1)
            else:
                value2 = values
                for current_value in current_values:
                    value1 = current_value
                    print '%s\t%s' % (current_key, value2 + "," + value1)
        elif current_tag == tag:
            current_values.append(values)
    else:
        current_values = [values]
        current_key = key
        current_tag = tag
