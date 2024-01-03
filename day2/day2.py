"""Solve day 2 puzzle: https://adventofcode.com/2023/day/2"""
from pathlib import Path
import re


def open_file(file_name: str):
    """Open file in the current directory and return a stream"""
    path = Path(__file__).with_name(file_name).absolute()
    return open(path, encoding="utf-8")


def solve_part_1(input_file_name: str, red: int, green: int, blue: int) -> int:
    """Solve part 1 of the puzzle"""
    file = open_file(input_file_name)
    result = 0
    for line in file:
        reds = [int(i) for i in re.findall(r" (\d+) red", line)]
        greens = [int(i) for i in re.findall(r" (\d+) green", line)]
        blues = [int(i) for i in re.findall(r" (\d+) blue", line)]
        if red >= max(reds) and green >= max(greens) and blue >= max(blues):
            game_id = re.search(r"Game (\d+):", line).group(1)
            result += int(game_id)  # wrong somewhere

    return result


def solve_part_2(input_file_name: str) -> int:
    """Solve part 2 of the puzzle"""
    file = open_file(input_file_name)
    result = 0
    for line in file:
        reds = [int(i) for i in re.findall(r" (\d+) red", line)]
        greens = [int(i) for i in re.findall(r" (\d+) green", line)]
        blues = [int(i) for i in re.findall(r" (\d+) blue", line)]
        power = max(reds) * max(greens) * max(blues)
        result += power
    return result


# print(solve_part_1("input_example.txt", 12, 13, 14))
# 8 is the correct answer
# print(solve_part_1("input.txt", 12, 13, 14))
# 2162 is the correct answer

# print(solve_part_2("input_example.txt"))
# 2286 is the correct answer
print(solve_part_2("input.txt"))
# 72513 is the correct answer
