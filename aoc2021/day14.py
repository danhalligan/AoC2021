from aoc2021.helpers import *
from collections import Counter, defaultdict

def data(file):
    polymer, rules = input_str(file).rstrip().split("\n\n")
    rules = dict(x.split(" -> ") for x in rules.split("\n"))
    return polymer, rules

def extend(polymer, rules):
    new = ''
    for i in range(len(polymer)-1):
        new += polymer[i] + rules[polymer[i]+polymer[i+1]]
    new += polymer[-1]
    return new

def part1(file):
    polymer, rules = data(file)
    for i in range(10):
        polymer = extend(polymer, rules)
    c = Counter(polymer).most_common()
    return c[0][1] - c[-1][1]

def extend2(map, letters, rules):
    new = defaultdict(int)
    for k, v in map.items():
        new[k[0] + rules[k]] += v
        new[rules[k] + k[1]] += v
        letters[rules[k]] += v
    return new, letters

# Count frequencies of pairs
def part2(file):
    polymer, rules = data(file)
    map = Counter(a + b for a, b in zip(polymer, polymer[1:]))
    letters = Counter(polymer)
    for i in range(40):
        map, letters = extend2(map, letters, rules)
    c = letters.most_common()
    return c[0][1] - c[-1][1]
