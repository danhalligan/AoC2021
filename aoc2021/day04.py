from aoc2021.helpers import *
import numpy as np

def data():
    x = open("inputs/day04.txt").read().split("\n\n")
    numbers = list(map(int, x[0].split(",")))
    boards = [Board(y) for y in x[1:]]
    return numbers, boards

class Board:
    def __init__(self, x):
        self.data = np.array([list(map(int, r.split())) for r in x.split("\n")])
        self.marks = np.array([[False]*5]*5)
    def fill(self, num):
        self.marks[np.where(self.data == num)] = True
    def winner(self):
        return np.any(np.all(self.marks, 0)) or np.any(np.all(self.marks, 1))
    def score(self, num):
        return np.sum(self.data[np.where(self.marks == False)]) * num

def part1():
    numbers, boards = data()
    for num in numbers:
        for board in boards:
            board.fill(num)
            if board.winner():
                return board.score(num)

def part2():
    numbers, boards = data()
    for num in numbers:
        for board in boards:
            board.fill(num)
            if all(b.winner() for b in boards):
                return board.score(num)
