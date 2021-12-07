from aoc2021.helpers import *
from collections import Counter
from operator import eq, ne

def best(x, i):
    c = Counter(x[i] for x in x).most_common()
    return "1" if (c[0][1] == c[1][1]) else c[0][0]

def as_int(x):
    return int(''.join(x), 2)

def invert(x):
    return [{'0': '1', '1': '0'}[c] for c in x]

def part1(file = input_file(3)):
    data = input_lines(file)
    gamma_rate = [best(data, i) for i in range(len(data[0]))]
    epsilon_rate = invert(gamma_rate)
    return as_int(gamma_rate) * as_int(epsilon_rate)

def filter(dat, fn):
    for i in range(len(dat[0])):
        b = best(dat, i)
        dat = [x for x in dat if fn(x[i], b)]
        if len(dat) == 1: return dat[0]

def part2(file = input_file(3)):
    data = input_lines(file)
    oxygen_generator_rating = filter(data, eq)
    co2_scrubber_rating = filter(data, ne)
    return as_int(oxygen_generator_rating) * as_int(co2_scrubber_rating)
