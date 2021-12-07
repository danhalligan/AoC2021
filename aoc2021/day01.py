from aoc2021.helpers import *

def n_increases(x):
    return sum(x[i] - x[i-1] > 0 for i in range(1, len(x)))

def part1(file = input_file(1)):
    return n_increases(input_ints(file))

def part2(file = input_file(1)):
    x = input_ints(file)
    sums = [(x[i] + x[i-1] + x[i-2]) for i in range(2, len(x))]
    return n_increases(sums)
