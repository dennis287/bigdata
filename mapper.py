#!/usr/bin/env python
"""mapper.py"""


import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    j = 0

    for word in words:
        if j == 0:
            country = word
        else:
            temp = word
        j = j + 1

    print('%s\t%s' % (country, temp))
