import os
import importlib
import pytest
from aoc2021.helpers import *

solutions = [
    (1, [7, 5]),
    (2, [150, 900]),
    (3, [198, 230]),
    (4, [4512, 1924]),
    (5, [5, 12]),
    (6, [5934, 26984457539]),
    (7, [37, 168]),
    (8, [26, 61229]),
    (9, [15, 1134]),
    (10, [26397, 288957]),
    (11, [1656, 195]),
    (12, [226, 3509]),
    (13, [17, open("tests/outputs/day13.txt").read()]),
    (14, [1588, 2188189693529])
]

# Test each day by importing the module and running part1 and part2
@pytest.mark.parametrize("day,expected", solutions)
def test_all(day, expected):
    module = importlib.import_module(f"aoc2021.day{day:02d}")
    file = "tests/inputs/day" + f'{day:02d}' + ".txt"
    assert getattr(module, 'part1')(file) == expected[0]
    assert getattr(module, 'part2')(file) == expected[1]
