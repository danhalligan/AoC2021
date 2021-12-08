from aoc2021.helpers import *
import numpy as np

def part1(file):
    dat = np.array(input_ints(file))
    return sum(abs(dat - int(np.median(dat))))

def part2(file):
    dat = np.array(input_ints(file))
    r = range(min(dat), max(dat) + 1)
    costs = np.array([sum(range(i+1)) for i in r])
    return min(sum(costs[abs(dat - i)]) for i in r)
