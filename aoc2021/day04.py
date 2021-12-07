from aoc2021.helpers import *
import numpy as np

def data(file):
    chunks = input_str(file).rstrip().split("\n\n")
    numbers = list(map(int, chunks[0].split(",")))
    boards = [Board(y) for y in chunks[1:]]
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

def play(numbers, boards, critera):
    for num in numbers:
        for board in boards:
            board.fill(num)
            if critera(board, boards):
                return board.score(num)

def part1(file = input_file(4)):
    numbers, boards = data(file)
    return play(numbers, boards, lambda board, _: board.winner())

def part2(file = input_file(4)):
    numbers, boards = data(file)
    return play(numbers, boards, lambda _, boards: all(b.winner() for b in boards))
