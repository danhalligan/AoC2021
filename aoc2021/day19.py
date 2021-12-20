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

def rotate_scanner(x):
    return zip(*[rotations(c) for c in x])

def data(file):
    dat = input_str(file)
    chunks = dat.split("\n\n")
    scanners = []
    for chunk in chunks:
        scanner = [tuple(map(int, l.split(','))) for l in chunk.splitlines()[1:]]
        scanners += [scanner]
    return scanners

def find_match(refset, s2):
    for rx in rotate_scanner(s2):
        # rx = np.array(rx)
        for p2 in rx:
            for p1 in refset:
                diff = (p1[0]-p2[0], p1[1]-p2[1], p1[2]-p2[2])
                count = 0
                for x in rx:
                    p  = (x[0]+diff[0], x[1]+diff[1], x[2]+diff[2])
                    if p in refset: count += 1
                    if count == 12:
                        tx = set([(x[0]+diff[0], x[1]+diff[1], x[2]+diff[2]) for x in rx])
                        return refset.union(tx), diff
    return None, None

file = "tests/inputs/day19.txt"
scanners = data(file)
ref = set(scanners[0])
tosearch = set(range(1, len(scanners)))
shifts = {}
shifts[0] = (0,0,0)
while len(tosearch):
    for i in tosearch:
        tot, shift = find_match(ref, scanners[i])
        if tot: break
    tosearch.remove(i)
    shifts[i] = shift
    ref = tot
    print("matched", i)


def part1(file):
    return len(ref)

def part2(file):
    best = 0
    for i in shifts.keys():
        for j in shifts.keys():
            x = shifts[i]
            y = shifts[j]
            best = max(best, sum(abs(x[i]-y[i]) for i in range(3)))
    return best
