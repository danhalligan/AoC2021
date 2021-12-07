from aoc2021.helpers import *
from collections import defaultdict
import re

def data(file):
    return [list(map(int, re.findall("\d+", y))) for y in input_lines(file)]

def drange(x, y):
    return range(x, y + 1, 1) if y >= x else range(x, y - 1, -1)

def n_overlaps(grid):
    return len([x for x in grid.values() if x > 1])

def part1(file = input_file(5)):
    grid = defaultdict(int)
    for x1, y1, x2, y2 in data(file):
        if x1 == x2:
            for i in drange(y1, y2): grid[x1, i] += 1
        elif y1 == y2:
            for i in drange(x1, x2): grid[i, y1] += 1
    return n_overlaps(grid)

def part2(file = input_file(5)):
    grid = defaultdict(int)
    for x1, y1, x2, y2 in data(file):
        if x1 == x2:
            for i in drange(y1, y2): grid[x1, i] += 1
        elif y1 == y2:
            for i in drange(x1, x2): grid[i, y1] += 1
        else:
            for x, y in zip(drange(x1, x2), drange(y1, y2)): grid[x, y] += 1
    return n_overlaps(grid)
