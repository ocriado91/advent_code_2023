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


def extract_round_results(data: list) -> dict:
    '''
    AoC Challenge Day#2
    --------------------------------
    Function to extract into a dictionary the results of each round
    '''

    results_by_game = {}
    for game in data:
        game_id, game_rounds = game.split(":")
        # Convert game ID to integer value
        game_id = int(game_id.split(" ")[1])

        # Build game results list
        game_rounds = game_rounds.split(";")
        # Round by round
        results_by_round = []
        for game_round in game_rounds:
            game_results = game_round.split(',')
            # Result by result
            results = {}
            for game_result in game_results:
                # Remove leading and trailing whitespaces
                game_result = game_result.strip()
                number, color = game_result.split(" ")
                results[color] = int(number)
            results_by_round.append(results)
        results_by_game[game_id] = results_by_round
    return results_by_game


def check_game_results(results: dict) -> list:
    '''
    AoC Day#2
    ---------------
    Check game results dictionary
    '''

    threshold = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    valid_games = []
    for game in results:
        valid_game = True
        for result in results[game]:
            for threshold_items in threshold.items():
                if threshold_items[0] in result.keys():
                    if result[threshold_items[0]] > threshold_items[1]:
                        valid_game = False
        if valid_game:
            valid_games.append(game)
        valid_game = True
    return valid_games


def check_minimum_cubes(results: dict) -> int:
    '''
    AoC Day#2
    -------------------
    Return the power of each game
    '''

    max_value = {}
    colors = ["red", "green", "blue"]
    power_games = []
    for game in results:
        round_id = 0
        max_value = {}
        for result in results[game]:
            round_id += 1
            for color in colors:
                if color not in max_value:
                    max_value[color] = 0
                if color in result.keys():
                    if result[color] > max_value[color]:
                        max_value[color] = result[color]
        power_game = 1
        for value in max_value.items():
            power_game = power_game * value[1]
        power_games.append(power_game)

    return sum(power_games)


def compute_neighbors(data: list,
                      start: int,
                      end: int,
                      row: int) -> list:
    '''
    Compute the neighborhood of an item within
    a matrix according with its horizontal and
    vertical indexes.

    Parameters:
        - data: Source matrix
        - start: horizontat begin index of item
        - end: horizontal end index of item
        - row: row number of index within the matrix

    Example: Neighborhood (/) of number 147
             within the matrix (|)

    -------------------------
    |.|.|.|+|.|./$/*/./././.|
    -------------------------
    |@|.|.|.|%|././1/4/7/./.|
    -------------------------
    |.|.|.|.|.|././././././.|
    -------------------------

        Params: start = 7; end = 9; row = 1

        Neighbors =
            -------------
            /$/*/./././.|
            -------------
            /./1/4/7/./.|
            -------------
            /./././././.|

    '''

    neighbors = []
    if start == 0:
        if row == 0:
            neighbors = [x[start:end+2] for x in data[row:row+2]]
        else:
            neighbors = [x[start:end+2] for x in data[row-1:row+2]]
    else:
        if row == 0:
            neighbors = [x[start-1:end+2] for x in data[row:row+2]]
        else:
            neighbors = [x[start-1:end+2] for x in data[row-1:row+2]]

    return neighbors


def adjacent_numbers(data: list) -> list:
    '''
    AoC - Day#3
    Compute adjacent numbers to a symbol
    '''

    valid_numbers = []
    number_pattern = r"\d+"
    symbol_pattern = r"[^a-zA-Z0-9.]"
    row = 0
    for line in data:
        start = -1
        number_matches = re.findall(number_pattern, line)
        for number in number_matches:
            start = line.index(number, start + 1)
            end = start + len(number)
            neighbors = compute_neighbors(data,
                                          start,
                                          end,
                                          row)
            if any(re.search(symbol_pattern, x) for x in neighbors):
                valid_numbers.append(int(number))
        row += 1

    return valid_numbers


def check_gears(data: list) -> list:
    '''
    Extract the gears (= any "*" symbol that is adjacent to
    exactly two part numbers) and computes their gear ratio
    '''

    candidate_gears = {}
    gear_ratios = []
    for row, line in enumerate(data):
        end = 0
        # Detect each number into incoming data to compute
        # its neighbor
        number_matches = re.findall(r"\d+", line)
        for number in number_matches:
            start = line.index(number, end)
            end = start + len(number) - 1
            neighbors = compute_neighbors(data,
                                          start,
                                          end,
                                          row)

            # Check if gear symbol (*) is within the number neighbor
            if any(x for x in neighbors if "*" in x):

                # Compute the X coordinate within the neighbor and extract its
                # global X coordinate according to current start variable
                x_position = [x.index("*") for x in neighbors
                              if "*" in x][0] + start
                if start != 0:
                    x_position -= 1

                # Compute the Y coordinate within the neighbor and extract its
                # global Y coordinate according with current number position
                # within the neighbor and current row
                gear_y_position = [idx for idx, x in enumerate(neighbors)
                                   if "*" in x][0]
                gear_number_position = [idx for idx, x in enumerate(neighbors)
                                        if number in x][0]
                y_position = row + gear_y_position - gear_number_position

                # Save the X,Y coordinates
                gear_position = (x_position, y_position)

                # Check if current gear position have been previously stored
                if gear_position in candidate_gears:
                    # Detected gear position, compute the ratio between
                    # previous number and current number
                    gear_ratios.append(int(number) *
                                       candidate_gears[gear_position])
                else:
                    # Stored gear position into candidates
                    candidate_gears[gear_position] = int(number)
        row += 1
    return gear_ratios


def extract_scratchcard_points(data: list) -> int:
    '''
    Compute the points of each scratchcard
    '''

    total_points = 0
    for line in data:
        # Extract the scratchcard numbers
        numbers = line.split(':')[1]

        # Split winning numbers and my numbers
        winning_numbers, my_numbers = numbers.split('|')

        # Convert string of numbers into list of numbers
        winning_numbers = winning_numbers.split()
        my_numbers = my_numbers.split()

        # Compute the intersection between two lists
        my_winning_numbers = list(set(winning_numbers) &
                                  set(my_numbers))

        # Each winning number duplicates the points
        points = 0
        if my_winning_numbers:
            points = 2 ** (len(my_winning_numbers) - 1)

        # Add scratchcard points to total
        total_points += points

    return total_points
