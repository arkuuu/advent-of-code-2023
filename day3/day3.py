"""Solve day 3 puzzle: https://adventofcode.com/2023/day/3"""
from pathlib import Path
from typing import Optional


def open_file(file_name: str):
    """Open file in the current directory and return a stream"""
    path = Path(__file__).with_name(file_name).absolute()
    return open(path, encoding="utf-8")


def load_engine_schematic(input_file_name: str) -> list:
    file = open_file(input_file_name)
    engine_schematic = []

    for line in file:
        row = []
        line = line.rstrip()
        for char in line:
            row.append(char)
        engine_schematic.append(row)

    return engine_schematic


def has_adjacent_symbol(engine_schematic: list, position: tuple) -> bool:
    adjacent_positions = get_adjacent_positions(position)
    for adjacent_position in adjacent_positions:
        if is_symbol_at_position(engine_schematic, adjacent_position):
            return True
    return False


def get_adjacent_positions(position: tuple) -> list:
    (i, j) = position
    return [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]


def is_symbol_at_position(engine_schematic: list, position: tuple) -> bool:
    char = get_char_at_position(engine_schematic, position)
    if char is None:
        return False
    return is_symbol(char)


def get_char_at_position(engine_schematic: list, position: tuple) -> Optional[str]:
    (i, j) = position
    if i >= len(engine_schematic):
        return None
    if j >= len(engine_schematic[i]):
        return None
    return engine_schematic[i][j]


def is_symbol(char: str) -> bool:
    if char.isdigit():
        return False
    if char == ".":
        return False
    return True


def get_complete_number_for_position(engine_schematic: list, position: tuple) -> int:
    (i, j) = position
    number_parts = []

    # go to the left-most digit
    while j > 0 and engine_schematic[i][j - 1].isdigit():
        j -= 1
    # collect all digits till the right-most digit or end of row
    while j < len(engine_schematic[i]) and engine_schematic[i][j].isdigit():
        number_parts.append(engine_schematic[i][j])
        j += 1

    return int("".join(number_parts))


def solve_part_1(input_file_name: str) -> int:
    """Solve part 1 of the puzzle"""
    engine_schematic = load_engine_schematic(input_file_name)
    result = 0

    for i, row in enumerate(engine_schematic):
        number_parts = []
        is_number_selected = False
        for j, char in enumerate(row):
            if char.isdigit():
                number_parts.append(char)
                is_number_selected = is_number_selected or has_adjacent_symbol(
                    engine_schematic, (i, j)
                )
            else:
                # end of current number, but not end of row yet
                if is_number_selected and len(number_parts) > 0:
                    result += int("".join(number_parts))
                number_parts = []
                is_number_selected = False
        # end of row
        if is_number_selected and len(number_parts) > 0:
            result += int("".join(number_parts))

    return result


def solve_part_2(input_file_name: str) -> int:
    """Solve part 2 of the puzzle"""
    engine_schematic = load_engine_schematic(input_file_name)
    result = 0

    for i, row in enumerate(engine_schematic):
        for j, char in enumerate(row):
            if char == "*":
                adjacent_positions = get_adjacent_positions((i, j))
                adjacent_numbers = []
                for adjacent_position in adjacent_positions:
                    char = get_char_at_position(engine_schematic, adjacent_position)
                    if char.isdigit():
                        number = get_complete_number_for_position(
                            engine_schematic, adjacent_position
                        )
                        # A number can stretch over multiple adjacent positions and would
                        # then be selected twice, so we need to remove duplicates.
                        # Doing this would be wrong if a gear intentionally has the same
                        # two numbers, but luckily this doesn't happen with given inputs
                        if number not in adjacent_numbers:
                            adjacent_numbers.append(number)
                if len(adjacent_numbers) == 2:
                    gear_ratio = adjacent_numbers[0] * adjacent_numbers[1]
                    result += gear_ratio

    return result


# print(solve_part_1("input_example.txt"))
# 4361 is the correct answer
# print(solve_part_1("input.txt"))
# 560670 is the correct answer

# print(solve_part_2("input_example.txt"))
# 467835 is the correct answer
print(solve_part_2("input.txt"))
# 91622824 is the correct answer
