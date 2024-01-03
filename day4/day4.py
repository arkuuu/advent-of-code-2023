"""Solve day 4 puzzle: https://adventofcode.com/2023/day/4"""
from pathlib import Path


def open_file(file_name: str):
    """Open file in the current directory and return a stream"""
    path = Path(__file__).with_name(file_name).absolute()
    return open(path, encoding="utf-8")


def count_matching_numbers(card: str) -> int:
    """Return the count of matching numbers for a card"""
    [_, numbers] = card.split(":")
    [winning_numbers, card_numbers] = numbers.split("|")
    winning_numbers = winning_numbers.split()
    card_numbers = card_numbers.split()

    count = 0
    for winning_number in winning_numbers:
        if winning_number in card_numbers:
            count += 1
    return count


def count_cards_recursive(cards: list, start: int, length: int) -> int:
    """Return the count of cards won"""
    if start > len(cards):
        return 0
    if start + length > len(cards):
        return 0

    count = 0
    for i in range(start, start + length):
        count += 1
        matching_numbers_count = count_matching_numbers(cards[i])
        if matching_numbers_count > 0:
            count = count + count_cards_recursive(cards, i + 1, matching_numbers_count)

    return count


def solve_part_1(input_file_name: str) -> int:
    """Solve part 1 of the puzzle"""
    file = open_file(input_file_name)
    overall_points = 0

    for line in file:
        card_matches = count_matching_numbers(line)
        if card_matches > 0:
            card_points = 2 ** (card_matches - 1)
            overall_points += card_points

    return overall_points


def solve_part_2(input_file_name: str) -> int:
    """Solve part 2 of the puzzle"""
    file = open_file(input_file_name)
    cards = file.readlines()

    return count_cards_recursive(cards, 0, len(cards))


# print(solve_part_1("input_example.txt"))
# 13 is the correct answer
# print(solve_part_1("input.txt"))
# 53491 is too high
# 20844 is too low
# 25651 is the correct answer

# print(solve_part_2("input_example.txt"))
# 30 is the correct answer
print(solve_part_2("input.txt"))
# 19499881 is the correct answer
