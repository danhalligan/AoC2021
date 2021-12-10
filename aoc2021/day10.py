from aoc2021.helpers import *

def data(file):
    return input_lines(file)

def pair(c):
    return {']':'[', ')':'(', '>':'<', '}':'{',
            '[':']', '(':')', '<':'>', '{':'}'}[c]

def score(c):
    return {')':3, ']':57, '}':1197, '>':25137}[c]

def part1(file):
    total = 0
    for line in data(file):
        stack = []
        for char in list(line):
            error = False
            if char in ['[', '(', '<', '{']:
                stack += [pair(char)]
            else:
                if len(stack) == 0 or stack.pop() != char:
                    total += score(char)
                    continue
    return total

def score2(c):
    return {')':1, ']':2, '}':3, '>':4}[c]

def part2(file):
    scores = []
    for line in data(file):
        stack = []
        for char in list(line):
            if char in ['[', '(', '<', '{']:
                stack += [pair(char)]
            else:
                if len(stack) == 0 or stack.pop() != char:
                    break
        else:
            ls = 0
            for s in stack[::-1]:
                ls = ls * 5 + score2(s)
            scores += [ls]
    scores.sort()
    return scores[len(scores) // 2]

