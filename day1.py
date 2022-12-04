#! /usr/bin/env python3

import sys

def part1():
    currMax = 0
    newMax = 0
    for line in sys.stdin:
        if (newMax > currMax):
            currMax = newMax

        if (line != '\n'):
            newMax += int(line)
        else:
            newMax = 0;
    print(currMax)

def part2():
    
    elfs = []
    cal = 0;

    for line in sys.stdin:
        if (line != '\n'):
            cal += int(line)
        else: 
            elfs.append(cal)
            cal = 0
    elfs.sort(reverse=True)
    print(sum(elfs[:3]))
