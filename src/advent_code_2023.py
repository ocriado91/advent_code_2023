#!/usr/bin/env python3
'''
Advent of Code (https://adventofcode.com/) is a set
of small daily code challenges like an advent Calendar
'''

from tools.tools import load_data, extract_digits, word_to_value


def solution_day_one_1_part_a(data: list) -> int:
    """
    Solution of first challenge of Advent of Code (Part A)
    """
    sum_data = 0
    for number in data:
        sum_data += extract_digits(number)

    return sum_data


def solution_day_one_1_part_b(data: list) -> int:
    """
    Solution of first challenge of Advent of Code (Part B)
    """
    sum_data = 0

    for number in data:
        sum_data += word_to_value(number)

    return sum_data


if __name__ == '__main__': # pragma: no cover
    day_one_data = load_data("data/puzzle_input_day_one.dat")
    print(f"Solution of day one (part A) = {solution_day_one_1_part_a(day_one_data)}")
    print(f"Solution of day one (part B) = {solution_day_one_1_part_b(day_one_data)}")
