from aoc2021.helpers import *
from functools import cache
import re

def data(file):
    s = input_str(file)
    return list(map(int, re.findall(": (\d+)", s)))

class Die:
    def __init__(self):
        self.throws = list(range(1, 101)) + [1, 2]
        self.pos = 0
        self.count = 0
    def roll(self):
        self.count += 3
        p = self.pos
        self.pos = (self.pos + 3) % 100
        return sum(self.throws[p:p+3])

# A player class to store position and score
# Requires hash and eq methods for caching
class Player:
    def __init__(self, start, score=0):
        self.pos = start
        self.score = score
    def update(self, roll):
        self.pos = (self.pos + roll - 1) % 10 + 1
        self.score += self.pos
    def clone(self):
        return Player(self.pos, self.score)
    def __eq__(self, other):
        return self.pos == other.pos and self.score == other.score
    def __hash__(self):
        return hash((self.pos, self.score))


def part1(file):
    s1, s2 = data(file)
    d = Die()
    players = [Player(s1), Player(s2)]
    p = 0
    while True:
        players[p].update(d.roll())
        if players[p].score >= 1000: break
        p = 1 if p == 0 else 0
    return min(x.score for x in players) * d.count

@cache
def play(players, p):
    wins = [0, 0]
    for throw, n in (3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1):
        curr = tuple([x.clone() for x in players])
        curr[p].update(throw)
        if curr[p].score >= 21:
            wins[p] += n
        else:
            w1, w2 = play(curr, 1 if p == 0 else 0)
            wins = [wins[0] + w1*n, wins[1] + w2*n]
    return wins

def part2(file):
    s1, s2 = data(file)
    wins = play((Player(s1), Player(s2)), 0)
    return max(wins)
