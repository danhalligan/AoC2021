from aoc2021.helpers import *

def data(file):
    x = re.findall("-*\d+", input_str(file))
    x = list(map(int, x))
    return [(x[0], x[1]), (x[2], x[3])]

def within(p, target):
    x, y = target
    return p[0] >= x[0] and p[0] <= x[1] and p[1] >= min(y) and p[1] <= max(y)

def probe_path(x, y, target):
    pos = [0,0]
    end = [max(target[0]), min(target[1])]
    hit = False
    top = 0
    while pos[0] < end[0] and (pos[1] > end[1] or y > 0):
        pos = [pos[0]+x, pos[1]+y]
        top = max(top, pos[1])
        if within(pos, target): hit = True
        if x > 0: x -= 1
        if x < 0: x += 1
        y -= 1
    return hit, top

def part1(file):
    target = data('inputs/day17.txt')
    best = 0
    for x in range(max(target[0])+1):
        for y in range(min(target[1]), 200):
            res, top = probe_path(x, y, target)
            if res: best = max(best, top)
    return best

def part2(file):
    target = data('inputs/day17.txt')
    count = 0
    for x in range(max(target[0])+1):
        for y in range(min(target[1]), 200):
            res, _ = probe_path(x, y, target)
            if res: count += 1
    return count








