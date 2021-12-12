from aoc2021.helpers import *
from collections import defaultdict, Counter

def create_map(file):
    map = defaultdict(list)
    for line in input_lines(file):
        a, b = line.split("-")
        map[a] += [b]
        map[b] += [a]
    return map

def good_route(visited):
    x = Counter(visited)
    x = [x[k] for k in x.keys() if k.islower() and x[k] > 1]
    return len(x) == 0

def good_route2(visited):
    x = Counter(visited)
    if x['start'] > 1: return False
    x = [x[k] for k in x.keys() if k.islower()]
    if any([v > 2 for v in x]): return False
    return sum(v > 1 for v in x) <= 1

def follow(map, fn, loc, visited):
    visited += [loc]
    if loc == 'end':
        yield visited
    else:
        for dest in map[loc]:
            if fn(visited):
                yield from follow(map, fn, dest, visited.copy())

def part1(file):
    map = create_map("inputs/day12.txt")
    return len(list(follow(map, good_route, 'start', [])))

def part2(file):
    map = create_map("inputs/day12.txt")
    return len(list(follow(map, good_route2, 'start', [])))
