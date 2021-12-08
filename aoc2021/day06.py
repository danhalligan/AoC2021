from aoc2021.helpers import *
from collections import Counter, defaultdict

def part1(file):
    dat = input_ints(file)
    for _ in range(80):
        dat = [x - 1 for x in dat]
        dat += [8] * dat.count(-1)
        dat = [6 if x == -1 else x for x in dat]
    return len(dat)

def part2(file):
    dat = Counter(input_ints(file))
    for _ in range(256):
        dat = defaultdict(int, [[k-1, dat[k]] for k in dat])
        dat[8] = dat[-1]
        dat[6] += dat.pop(-1)
    return sum(dat.values())
