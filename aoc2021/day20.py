from re import A
from aoc2021.helpers import *
from collections import defaultdict

def as_int(x):
    return [y == "#" for y in x]

def data(file):
    dat = input_str(file)
    chunks = dat.split("\n\n")
    return as_int(chunks[0]), [as_int(x) for x in chunks[1].split('\n')]

def neighbours(pos):
    i,j = pos
    return [
        (i-1, j-1), (i, j-1), (i+1, j-1),
        (i-1, j),   (i, j),   (i+1, j),
        (i-1, j+1), (i,j+1),  (i+1, j+1)
    ]

def enhance(image, default, algorithm):
    out = defaultdict(lambda: default)
    r1 = min(x for x, y in image.keys()) - 2
    r2 = max(x for x, y in image.keys()) + 2
    c1 = min(y for x, y in image.keys()) - 2
    c2 = max(y for x, y in image.keys()) + 2
    for r in range(r1, r2):
        for c in range(c1, c2):
            pos = (c,r)
            num = [str(int(image[p])) for p in neighbours(pos)]
            num = int(''.join(num), 2)
            out[pos] = algorithm[num]
    return out

def image_to_dict(x):
    out = defaultdict(bool)
    for r in range(len(x)):
        for c in range(len(x[r])):
            out[(r,c)] = x[c][r]
    return out

# This assumes that the algorithm converts the infinite dark pixels to light
# and vice versa each iteration...
def part1(file):
    algorithm, image = data(file)
    image = image_to_dict(image)
    image = enhance(image, True, algorithm)
    image = enhance(image, False, algorithm)
    return sum(image.values())

def part2(file):
    algorithm, image = data(file)
    image = image_to_dict(image)
    for i in range(25):
        image = enhance(image, True, algorithm)
        image = enhance(image, False, algorithm)
    return sum(image.values())



