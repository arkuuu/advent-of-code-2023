"""Solve day 1 puzzle: https://adventofcode.com/2023/day/1"""
from pathlib import Path
import re


def open_file(file_name: str):
    """Open file in the current directory and return a stream"""
    path = Path(__file__).with_name(file_name).absolute()
    return open(path, encoding="utf-8")


def solve_part_1(input_file_name: str) -> int:
    """Solve part 1 of the puzzle"""
    file = open_file(input_file_name)
    result = 0
    for line in file:
        numbers = re.findall(r"\d", line)
        if len(numbers) < 1:
            continue
        first_and_last_number = [numbers[0], numbers[-1]]
        combined_number = "".join(first_and_last_number)
        result += int(combined_number)
    file.close()
    return result


def solve_part_2(input_file_name: str) -> int:
    """Solve part 2 of the puzzle"""
    file = open_file(input_file_name)
    result = 0
    for line in file:
        line = replace_first_numerical_string_with_digit(line)
        line = replace_last_numerical_string_with_digit(line)
        numbers = re.findall(r"\d", line)
        if len(numbers) < 1:
            continue
        first_and_last_number = [numbers[0], numbers[-1]]
        combined_number = "".join(first_and_last_number)
        result += int(combined_number)
    file.close()
    return result


def replace_first_numerical_string_with_digit(string: str) -> str:
    replacements = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    return re.sub(
        r"(one|two|three|four|five|six|seven|eight|nine)",
        lambda m: replacements.get(m.group(0)),
        string,
        1,
    )


def replace_last_numerical_string_with_digit(string: str) -> str:
    replacements = {
        "eno": "1",
        "owt": "2",
        "eerht": "3",
        "ruof": "4",
        "evif": "5",
        "xis": "6",
        "neves": "7",
        "thgie": "8",
        "enin": "9",
    }

    string = re.sub(
        r"(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)",  # todo: build from replacements
        lambda m: replacements.get(m.group(0)),
        string[::-1],
        1,
    )

    return string[::-1]


# print(solve_part_1("input_example_part1.txt"))
# 142 is the correct answer

# print(solve_part_1("input.txt"))
# 53974 is the correct answer

# print(solve_part_2("input_example_part2.txt"))
# 281 is the correct answer

print(solve_part_2("input.txt"))
# 52840 is the correct answer
