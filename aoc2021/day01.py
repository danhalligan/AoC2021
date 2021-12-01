from aoc2021.helpers import *

def data():
    return list(map(int, input().split()))

def n_increases(x):
    return sum(x[i] - x[i-1] > 0 for i in range(1, len(x)))

def part1():
    return n_increases(data())

def part2():
    x = data()
    sums = [(x[i] + x[i-1] + x[i-2]) for i in range(2, len(x))]
    return n_increases(sums)
