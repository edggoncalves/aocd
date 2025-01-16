from os import remove

from input import get_data, get_input


class Tests:
    def __init__(self, line: list[int], tolerance: int = 0):
        self.line = line
        self.increasing = self.is_increasing()
        self.decreasing = self.is_decreasing()
        self.safe = self.safe_difference()

    def is_increasing(self) -> bool:
        for i in range(len(self.line)-1):
            if self.line[i] > self.line[i+1]:
                return False
        return True

    def is_decreasing(self) -> bool:
        for i in range(len(self.line)-1):
            if self.line[i] < self.line[i+1]:
                return False
        return True

    def safe_difference(self) -> bool:
        for i in range(len(self.line)-1):
            val = abs(self.line[i] - self.line[i+1])
            if val > 3 or val == 0:
                return False
        return True


def part_one(input_data: list[str]) -> int:
    input_data = [[int(number) for number in line.split()] for line in input_data]
    result = 0

    for line in input_data:
        test = Tests(line)
        if any([test.increasing, test.decreasing]) and test.safe:
            result += 1
    return result


def part_two(input_data: list[str]) -> int:
    input_data = [[int(number) for number in line.split()] for line in input_data]
    result = 0

    for line in input_data:
        for i in range(len(line)):
            line_test = line.copy()
            line_test.pop(i)
            test = Tests(line_test)
            if any([test.increasing, test.decreasing]) and test.safe:
                result += 1
                break
    return result


if __name__ == '__main__':
    day, year = "2", "2024"
    get_input(day=day, year=year)
    data = get_data(input_data="data", year=year, day=day)
    # data = get_data(input_data="sample_data", year=year, day=day)
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")
