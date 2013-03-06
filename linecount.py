#!/usr/bin/env python
# Line count of a file

import sys

name = sys.argv[1]

def count(filename):
    lines = 0
    for line in open(filename):
        lines += 1
    return lines

linecount = count(name)

print name, "line count is: ", linecount

#raw_input("press any key to exit")