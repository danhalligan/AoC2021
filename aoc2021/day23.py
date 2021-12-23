from aoc2021.helpers import *

# Quicker (for me) to slve by hand.
# These are the moves...

def part1(file):
    A = 1
    B = 10
    C = 100
    D = 1000
    return A*8 + B*3 + D*5 + D*8 + A*3 + B*2 + C*6 + B*3 + C*7 + A*3 + A*6 + B*6

def part2(file):
    A = 1
    B = 10
    C = 100
    D = 1000
    return A*9 + A*9 + C*5 + B*5 + D*7 + D*10 + D*10 + D*10 + C*9 + A*5 + A*5 + B*7 + A*9 + A*9 + C*5 + B*4 + C*7 + B*4 + C*8 + B*5 + B*6 + B*5 + B*6 + C*5
