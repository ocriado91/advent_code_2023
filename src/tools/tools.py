#!/usr/bin/env python3
'''
Tool functions for Advent of Code 2023
'''

import re


def load_data(datafile: str) -> list:
    """
    Reads the contents of a file specified
    by the `datafile` parameter and returns
    the data as a list of strings.
    """
    with open(datafile, encoding="utf-8") as filereader:
        data = filereader.readlines()

    # Remove newline characters
    data = [line.strip("\n") for line in data]
    return data


def extract_digits(data: str) -> int:
    '''
    Extract the first and last digits
    of a string to form a 2-digits number
    '''

    # Use regex expresion to extract all number characters
    numbers = re.findall(r"\d", data)

    # Convert them to integer type
    numbers_list = list(map(int, numbers))

    # Extract the first (and use it as ten) and last digits
    return numbers_list[0] * 10 + numbers_list[-1]


def word_to_value(data: str) -> int:
    '''
    Convert number word to value
    '''

    number_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
    extracted_result = re.findall(pattern, data)
    result = []
    for items in extracted_result:
        if items in number_dict:
            result.append(number_dict[items])
        else:
            result.append(int(items))

    return result[0] * 10 + result[-1]
