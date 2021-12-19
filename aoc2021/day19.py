from aoc2021.helpers import *
from itertools import permutations
from functools import cache
import numpy as np

def rotations(p):
    x,y,z = p
    return [
        (x, y, z),
        (y, -x, z),
        (-x, -y, z),
        (-y, x, z),
        (z, y, -x),
        (y, -z, -x),
        (-z, -y, -x),
        (-y, z, -x),
        (-x, y, -z),
        (y, x, -z),
        (x, -y, -z),
        (-y, -x, -z),
        (-z, y, x),
        (y, z, x),
        (z, -y, x),
        (-y, -z, x),
        (x, z, -y),
        (z, -x, -y),
        (-x, -z, -y),
        (-z, x, -y),
        (x, -z, y),
        (-z, -x, y),
        (-x, z, y),
        (z, x, y)
    ]

# @cache
def rotate_scanner(x):
    return zip(*[rotations(c) for c in x])

def find_match(s1, s2):
    ref = np.array(s1)
    refset = set([tuple(x) for x in ref])
    s2 = tuple(tuple(x) for x in s2)
    for rx in rotate_scanner(s2):
        rx = np.array(rx)
        for p2 in rx:
            for p1 in ref:
                diff = p1 - p2
                tx = set([tuple(diff + x) for x in rx])
                n = len(refset.intersection(tx))
                if n >= 12:
                    return refset.union(tx), diff
    return None, None


file = "inputs/day19.txt"
dat = input_str(file)
chunks = dat.split("\n\n")
scanners = []
for chunk in chunks:
    scanner = [list(map(int, l.split(','))) for l in chunk.splitlines()[1:]]
    scanners += [scanner]

ref = scanners[0]
tosearch = set(range(1, len(scanners)))
shifts = {}
shifts[0] = np.array([0,0,0])
while len(tosearch):
    found = None
    for i in tosearch:
        tot, shift = find_match(ref, scanners[i])
        if tot:
            found = i
            break
    tosearch.remove(found)
    shifts[i] = shift
    ref = list(tot)
    print(shift, i, len(ref))


def part1(file):
    return len(ref)

def part2(file):
    best = 0
    for i in shifts.keys():
        for j in shifts.keys():
            best = max(best, sum(abs(shifts[i] - shifts[j])))
    return best

