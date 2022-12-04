#! /usr/bin/env python3

lookup = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2, 
    "Z": 3,
}

total = 0

with open('input/02', 'r') as file:
    for line in file:
        x = line.split()
        print(x)