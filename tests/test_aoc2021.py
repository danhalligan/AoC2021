from aoc2021 import __version__
import os
import importlib
import pytest

os.environ['PYTEST'] = 'true'

solutions = [
    (1, [7, 5]),
    (2, [150, 900]),
    (3, [198, 230]),
    (4, [4512, 1924]),
    (5, [5, 12]),
    (6, [5934, 26984457539])
]

# Test each day by importing the module and running part1 and part2
@pytest.mark.parametrize("day,expected", solutions)
def test_all(day, expected):
    module = importlib.import_module(f"aoc2021.day{day:02d}")
    assert getattr(module, 'part1')() == expected[0]
    assert getattr(module, 'part2')() == expected[1]
