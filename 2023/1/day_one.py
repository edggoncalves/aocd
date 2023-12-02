from input import get_data
import re


NUMBERS = {
    "zero": 0,
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


def _get_first_and_last_numbers(input_data: str) -> int:
    numbers = re.findall(pattern=r"\d", string=input_data)
    number = int("".join((numbers[0], numbers[-1])))
    return number


def _find_left_number(line: str) -> str:
    line = list(line)
    word = ""
    regex = "(" + ")|(".join(NUMBERS.keys()) + ")"
    for _ in range(len(line)):
        piece = line.pop(0)
        if piece.isdigit():
            return piece
        word += piece
        s = re.search(pattern=regex, string=word)
        if s:
            return str(NUMBERS[s.group()])


def _find_right_number(line: str) -> str:
    line = list(line)
    word = list()
    regex = "(" + ")|(".join(NUMBERS.keys()) + ")"
    for _ in range(len(line)):
        piece = line.pop(-1)
        if piece.isdigit():
            return piece
        word.insert(0, piece)
        word_str = "".join(word)
        s = re.search(pattern=regex, string=word_str)
        if s:
            return str(NUMBERS[s.group()])


def part_one(input_data: list[str]) -> int:
    total = 0
    for line in input_data:
        number: int = _get_first_and_last_numbers(input_data=line)
        total += number
    return total


def part_two(input_data: list[str]) -> int:
    total = 0
    for line in input_data:
        left_number = _find_left_number(line=line)
        right_number = _find_right_number(line=line)
        number = int(f"{left_number}{right_number}")
        total += number
    return total


if __name__ == '__main__':
    data = get_data(input_data="day_one", year="2023", day="1")
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")
