#!/usr/bin/env python3
'''
Testing functions to check Advent of Code
methods and functions
'''

from advent_code_2023 import load_data,\
                             extract_digits,\
                             word_to_value,\
                             solution_day_one_1_part_a,\
                             solution_day_one_1_part_b,\
                             solution_day_two_part_a,\
                             solution_day_two_part_b

from tools.tools import extract_round_results,\
                        check_game_results,\
                        check_minimum_cubes


def test_load_data():
    '''
    Check loaded data from incoming data
    '''

    data = load_data("test/data/puzzle_test.dat")
    assert data[0] == "1abc2"
    assert data[1] == "pqr3stu8vwx"
    assert data[2] == "a1b2c3d4e5f"
    assert data[3] == "treb7uchet"


def test_extract_digits():
    '''
    Check conversion to number values from incoming data
    '''
    data = load_data("test/data/puzzle_test.dat")
    assert extract_digits(data[0]) == 12
    assert extract_digits(data[1]) == 38
    assert extract_digits(data[2]) == 15
    assert extract_digits(data[3]) == 77


def test_word_to_value():
    '''
    Check conversion from number string to value
    '''
    data = load_data("test/data/puzzle_test2.dat")
    assert word_to_value(data[0]) == 29
    assert word_to_value(data[1]) == 83
    assert word_to_value(data[2]) == 13
    assert word_to_value(data[3]) == 24
    assert word_to_value(data[4]) == 42
    assert word_to_value(data[5]) == 14
    assert word_to_value(data[6]) == 76


def test_word_to_value_change_digits():
    '''
    Check conversion and extract first and last digits
    '''
    data = load_data("test/data/puzzle_test2.dat")
    assert word_to_value(data[0]) == 29
    assert word_to_value(data[1]) == 83
    assert word_to_value(data[2]) == 13
    assert word_to_value(data[3]) == 24
    assert word_to_value(data[4]) == 42
    assert word_to_value(data[5]) == 14
    assert word_to_value(data[6]) == 76


def test_extract_round_results():
    '''
    AoC Day#2
    ----------------------
    Test correct extraction of round results
    '''
    data = load_data("test/data/game_test.dat")
    results = extract_round_results(data)
    assert len(results) == 5


def test_check_game_results():
    '''
    Aoc Day#2
    --------------------
    Test correct check of game results dictionary
    '''

    data = load_data("test/data/game_test.dat")
    results = extract_round_results(data)
    valid_games = check_game_results(results)
    assert len(valid_games) == 3


def test_check_minimum_cubes():
    '''
    AoC Day#2
    ------------------
    Test power minimum cubes power function
    '''

    data = load_data("test/data/game_test.dat")
    results = extract_round_results(data)
    power_games = check_minimum_cubes(results)
    assert power_games == 2286


def test_solution_day_two_part_a():
    '''
    AoC Day#2
    ------------------
    Test solution day 2 (part A)
    '''

    data = load_data("test/data/game_test.dat")
    result = solution_day_two_part_a(data)
    assert result == 8


def test_solution_day_two_part_b():
    '''
    AoC Day#2
    ------------------
    Test solution day 2 (part B)
    '''

    data = load_data("test/data/game_test.dat")
    result = solution_day_two_part_b(data)
    assert result == 2286


def test_solution_day_one_part_a():
    '''
    Check Day One - Part A solution against expected solution according
    challenge's instrucctions
    '''

    data = load_data("test/data/puzzle_test.dat")
    solution = solution_day_one_1_part_a(data)
    assert solution == 142


def test_solution_day_one_part_b():
    '''
    Check Day One - Part B solution against expected solution according
    challenge's instrucctions
    '''

    data = load_data("test/data/puzzle_test2.dat")
    solution = solution_day_one_1_part_b(data)
    assert solution == 281
