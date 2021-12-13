from aoc2021.helpers import *
from collections import defaultdict, Counter

def create_map(file):
    map = defaultdict(list)
    for line in input_lines(file):
        a, b = line.split("-")
        map[a] += [b]
        map[b] += [a]
    return map

def valid(visited):
    x = Counter(visited)
    x = [x[k] for k in x.keys() if k.islower() and x[k] > 1]
    return len(x) == 0

def valid2(visited):
    x = Counter(visited)
    if x['start'] > 1: return False
    x = [x[k] for k in x.keys() if k.islower()]
    if max(x) > 2: return False
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
    map = create_map(file)
    return len(list(follow(map, valid, 'start', [])))

def part2(file):
    map = create_map(file)
    return len(list(follow(map, valid2, 'start', [])))
