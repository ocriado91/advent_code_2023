#!/usr/bin/env python3
'''
Advent of Code (https://adventofcode.com/) is a set
of small daily code challenges like an advent Calendar
'''

from tools.tools import load_data,\
                        extract_digits,\
                        word_to_value,\
                        extract_round_results,\
                        check_game_results,\
                        check_minimum_cubes


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


def solution_day_two_part_a(data: list) -> int:
    '''
    Solution of the AoC Day#2 (Part A)
    '''

    results = extract_round_results(data)
    valid_games = check_game_results(results)
    return sum(valid_games)


def solution_day_two_part_b(data: list) -> int:
    '''
    Solution of the AoC Day#2 (Part B)
    '''

    results = extract_round_results(data)
    return check_minimum_cubes(results)


if __name__ == '__main__':  # pragma: no cover
    # Day 1
    day_one_data = load_data("data/puzzle_input_day_one.dat")
    print(f"Day one (A) = {solution_day_one_1_part_a(day_one_data)}")
    print(f"Day one (B) = {solution_day_one_1_part_b(day_one_data)}")

    # Day 2
    day_two_data = load_data("data/puzzle_input_day_two.dat")
    print(f"Day two (A) = {solution_day_two_part_a(day_two_data)}")
    print(f"Day two (B) = {solution_day_two_part_b(day_two_data)}")
