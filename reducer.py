#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
occ_count = 0

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    count = int(count)

    if current_word == word:
        current_count += count
        occ_count += 1
    else:
        if current_word:
            print ('%s\t%s' % (current_word, current_count/occ_count))
        current_count = count
        current_word = word
        occ_count = 1

if current_word == word:
    print ('%s\t%s' % (current_word, current_count/occ_count))
