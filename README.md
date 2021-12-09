<!-- README.md is generated from README.Rmd. Please edit that file -->
# AoC2021

`AoC2021` is a set of python solutions for the
[Advent of Code 2021](https://adventofcode.com/2021) problems.

## Example

To solve a specific day, you can use `solve`, passing in the input file for
the current day using poetry.

``` bash
poetry run aoc2021 inputs/day01.txt
```

Or pass in multiple days to solve multiple inputs.

``` bash
poetry run aoc2021 inputs/*
```

You can automatically download the input for a given day by setting your
[session cookie] in an environment variable:

``` bash
export AOC_SESSION=[your session]
```

Then using the helper function, e.g. for today's input:

```python
> from aoc2021.helpers import *
> get_input()
```

[session cookie]: https://www.reddit.com/r/adventofcode/comments/a2vonl/how_to_download_inputs_with_a_script/
