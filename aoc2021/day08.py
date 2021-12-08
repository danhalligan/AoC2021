from aoc2021.helpers import *
from collections import Counter
import numpy as np

def data(file):
    dat = input_lines(file)
    return [[y.split() for y in x.split(" | ")] for x in dat]

def digit_encoding():
    return {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4,
        'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}

# solve a mapping with sufficient information.
# This works by looking for cases where a key maps to a singal value, it
# then removes this value from any other values.
def prune_map(map):
    for k in map.keys():
        if len(map[k]) == 1:
            for k2 in set(map.keys()) - set(k):
                map[k2] = list(set(map[k2]) - set(map[k]))
    return map

# We can apply rules to work out which signal should be which.
# The following rules are sufficient
# e will have count of 4
# b will have count of 6
# f will have count of 9
# c is within a digit with 2 signals on (1)
# a will be within a digit with three signals on (7)
# d will be within a digit with four signals on (4)
def build_map(wires):
    wires = [sorted(list(x)) for x in wires]
    lengths = [len(x) for x in wires]
    count = Counter(np.concatenate([list(x) for x in wires]))
    map = {
        'e': [k for k in count.keys() if count[k] == 4],
        'b': [k for k in count.keys() if count[k] == 6],
        'f': [k for k in count.keys() if count[k] == 9],
        'c': wires[lengths.index(2)],
        'a': wires[lengths.index(3)],
        'd': wires[lengths.index(4)],
        'g': ['a','b','c','d','e','f','g']
    }
    map = prune_map(prune_map(map))
    # invert map
    return dict([[map[x][0], x] for x in map.keys()])

def decode_digits(digits, map):
    digits = [''.join(sorted([map[y] for y in list(x)])) for x in digits]
    return [digit_encoding()[x] for x in digits]

def part1(file):
    res = [decode_digits(d, build_map(w)) for w, d in data(file)]
    counts = Counter(np.concatenate(res))
    return sum(counts[x] for x in [1,4,7,8])

def part2(file):
    res = [decode_digits(d, build_map(w)) for w, d in data(file)]
    return sum(int(''.join([str(y) for y in x])) for x in res)


# #-------------------------------------------------------------------------------
# # solution 2
# #-------------------------------------------------------------------------------

# # Each digit has a unique value based on the sum of the frequency of the
# # the signals. For example, c occurs 8 and f occurs 9 times above, so the
# # digit 1 can be represented as 8 + 9 = 17 (which is unique)

# # First create a map from unqiue sum to digit
# def digit_sums():
#     enc = digit_encoding()
#     counts = Counter(np.concatenate([list(x) for x in enc.keys()]))
#     return dict([[sum(counts[y] for y in list(x)), x] for x in enc.keys()])

# # To decode, we use hash lookup from the unique sums
# def decode(wires, digits):
#     enc = digit_encoding()
#     lookup = digit_sums()
#     wires = [sorted(list(x)) for x in wires]
#     digits = [''.join(sorted(list(x))) for x in digits]
#     count = Counter(np.concatenate(wires))
#     map = dict([''.join(x), lookup[sum(count[y] for y in x)]] for x in wires)
#     return [enc[map[digit]] for digit in digits]

# # # part 1
# def part1(file):
#     res = [decode(wires, digits) for wires, digits in data(file)]
#     counts = Counter(np.concatenate(res))
#     return counts[1] + counts[4] + counts[7] + counts[8]

# # # part 2
# def part2(file):
#     res = [decode(wires, digits) for wires, digits in data(file)]
#     return sum(int(''.join([str(y) for y in x])) for x in res)
