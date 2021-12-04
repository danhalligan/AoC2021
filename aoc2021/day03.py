from aoc2021.helpers import *
from collections import Counter
from operator import eq, ne

def data():
    return input().splitlines()

def best(x, i):
    c = Counter(x[i] for x in x).most_common()
    return "1" if (c[0][1] == c[1][1]) else c[0][0]

def as_int(x):
    return int(''.join(x), 2)

def invert(x):
    return [{'0': '1', '1': '0'}[c] for c in x]

def part1():
    m = [best(data(), i) for i in range(12)]
    return as_int(m) * as_int(invert(m))

def filter(dat, fn):
    for i in range(12):
        b = best(dat, i)
        dat = [x for x in dat if fn(x[i], b)]
        if len(dat) == 1: return dat[0]

def part2():
    m = filter(data(), eq)
    l = filter(data(), ne)
    return as_int(m) * as_int(l)
