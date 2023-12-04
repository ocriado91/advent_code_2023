#!/usr/bin/env python3
'''
Testing functions to check Advent of Code
methods and functions
'''

from advent_code_2023 import load_data,\
                             extract_digits,\
                             word_to_value,\
                             solution_day_one_1_part_a,\
                             solution_day_one_1_part_b


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
