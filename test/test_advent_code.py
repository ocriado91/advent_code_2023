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
                             solution_day_two_part_b,\
                             solution_day_three_part_a,\
                             solution_day_three_part_b,\
                             solution_day_four_part_a

from tools.tools import extract_round_results,\
                        check_game_results,\
                        check_minimum_cubes,\
                        adjacent_numbers,\
                        compute_neighbors,\
                        check_gears,\
                        extract_scratchcard_points


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


def test_compute_neighbors():
    '''
    Check the computation of neighbors
    within the source matrix according
    with item indexes
    '''

    source_matrix = [
        [".", ".", ".", "+", ".", ".", "$", "*", ".", ".", "."],
        ["@", ".", ".", ".", "%", ".", ".", "1", "4", "7", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]

    expected_neighbor = [
        ["$", "*", ".", ".", "."],
        [".", "1", "4", "7", "."],
        [".", ".", ".", ".", "."],
    ]

    neighbor = compute_neighbors(source_matrix,
                                 start=7,
                                 end=9,
                                 row=1)
    assert expected_neighbor == neighbor


def test_check_number_position():
    '''
    AoC Day#3 - Check start and end
    positions into a string
    '''

    data = load_data("test/data/day3_test.dat")
    valid_numbers = adjacent_numbers(data)
    assert valid_numbers[0] == 467
    assert valid_numbers[1] == 35


def test_solution_day_three_part_a():
    '''
    AoC Day#3 - Test the expected solution of AoC
    challenge
    '''

    data = load_data("test/data/day3_test.dat")
    result = solution_day_three_part_a(data)
    assert result == 4361


def test_solution_day_three_part_b():
    '''
    AoC Day#3 - Test the expected solution of AoC
    challenge
    '''

    data = load_data("test/data/day3_test.dat")
    result = solution_day_three_part_b(data)
    assert result == 467835


def test_check_gears():
    '''
    AoC Day#3 - Test the gears check function
    according with test data
    '''

    expected_gears = [16345, 451490]
    expected_sum = sum(expected_gears)
    data = load_data("test/data/day3_test.dat")
    gears = check_gears(data)
    assert expected_gears == gears
    assert expected_sum == sum(gears)


def test_check_gears_duplicates_line():
    '''
    AoC Day#3 - Check detection of gears
    into a line with multiple gears
    candidates
    '''

    expected_gears = [16345, 72162, 451490]
    expected_sum = sum(expected_gears)
    data = load_data("test/data/day3_test_custom.dat")
    gears = check_gears(data)
    assert expected_gears == gears
    assert expected_sum == sum(gears)


def test_check_gears_single_digits():
    '''
    AoC Day#3 - Check detection of gears into single
    digit numbers
    '''

    expected_sum = 3366664
    data = load_data("test/data/day3_test_custom2.dat")
    gears = check_gears(data)
    assert expected_sum == sum(gears)


def test_scratchcard():
    '''
    AoC Day#4 - Check scratchcard points of test data
    '''

    expected_scratchcard_points = 13
    data = load_data("test/data/day4_test_scratchcard.dat")
    scratchcard_points = extract_scratchcard_points(data)
    assert expected_scratchcard_points == scratchcard_points


# Integration tests

def test_example_solution_day_four_part_a():
    '''
    Check expected result according of AoC Day#4 - Part A
    according to example input
    '''

    expected_points = 13
    data = load_data("test/data/day4_test_scratchcard.dat")
    points = solution_day_four_part_a(data)
    assert expected_points == points


def test_solution_day_four_part_a():
    '''
    Check expected result according of AoC Day#4 - Part A
    according to example input
    '''

    expected_points = 24175
    data = load_data("data/puzzle_input_day_four.dat")
    points = solution_day_four_part_a(data)
    assert expected_points == points
