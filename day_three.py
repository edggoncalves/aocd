from statistics import mode
from collections import Counter


def _config() -> list:
    with open('data_day3.txt', 'r') as data:
        instructions = [f'0o{line}' for line in data.read().splitlines()]

    return instructions


def part_one(data):
    gamma = ''
    epsilon = ''
    loops = list(range(len(data[0][2:])))
    for loop in loops:
        current_bin = []
        for number in data:
            bit = number[2:][loop]
            current_bin.append(bit)
        gamma += mode(current_bin)
        epsilon += Counter(current_bin).most_common()[-1][0]

    return int(gamma, 2) * int(epsilon, 2)


def part_two(data):
    oxygen = ''
    co2 = ''
    return data


def main():
    data = [
        '0o00100', '0o11110', '0o10110', '0o10111', '0o10101', '0o01111', '0o00111', '0o11100', '0o10000', '0o11001',
        '0o00010', '0o01010'
    ]

    # data = _config()
    result_one = part_one(data)
    result_two = part_two(data)
    print(f'Part one: {result_one}')
    print(f'Part two: {result_two}')


if __name__ == '__main__':
    main()
