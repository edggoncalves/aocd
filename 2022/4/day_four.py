# sample_data = [
#     '2-4,6-8',
#     '2-3,4-5',
#     '5-7,7-9',
#     '2-8,3-7',
#     '6-6,4-6',
#     '2-6,4-8',
# ]


def get_range(line: str) -> tuple:
    ranges = line.split(',')

    r1 = [int(n) for n in ranges[0].split('-')]
    r1 = list(range(r1[0], (r1[1] + 1)))

    r2 = [int(n) for n in ranges[1].split('-')]
    r2 = list(range(r2[0], (r2[1] + 1)))

    return r1, r2


def part_one(data: list) -> int:
    overlap = 0

    for line in data:
        r1, r2 = get_range(line)
        if all(i in r2 for i in r1) or all(i in r1 for i in r2):
            overlap += 1

    return overlap


def part_two(data: list) -> int:
    overlap = 0

    for line in data:
        r1, r2 = get_range(line)
        if len(list(set(r1) & set(r2))) > 0:
            overlap += 1
    return overlap


def main():
    with open('day_four.txt', 'r') as f:
        data = f.read().splitlines()
    part_1 = part_one(data)
    part_2 = part_two(data)

    print(f'Part One: {part_1}')
    print(f'Part Two: {part_2}')


if __name__ == '__main__':
    main()
