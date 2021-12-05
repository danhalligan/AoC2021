# Functions to help read inputs

def input_str(day):
    return open("inputs/day" + f'{day:02d}' + ".txt", 'r').read()

def input_lines(day):
    return input_str(day).splitlines()

def input_ints(day):
    return list(map(int, input_str(day).split()))
