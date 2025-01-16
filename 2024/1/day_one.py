from input import get_data

def _split_data(input_data: list[str]) -> tuple[list[int], list[int]]:
    left = [int(i.split()[0]) for i in input_data]
    right = [int(i.split()[1]) for i in input_data]
    return left, right


def part_one(input_data: list[str]) -> int:
    left, right = _split_data(input_data)
    result = 0
    for i in range(len(left)):
        r = abs(left.pop(left.index(min(left))) - right.pop(right.index(min(right))))
        result += r
    return result


def part_two(input_data: list[str]) -> int:
    left, right = _split_data(input_data)
    similarity = 0
    similarity += sum([i*right.count(i) for i in left if i in right])
    return similarity

if __name__ == '__main__':
    data = get_data(input_data="day_one", year="2024", day="1")
    # data = get_data(input_data="sample_data", year="2024", day="1")
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")
