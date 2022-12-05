# sample_data = {
#     'A': 'Y',
#     'B': 'X',
#     'C': 'Z'
# }

SCORING = {
    'AX': 4,
    'AY': 8,
    'AZ': 3,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 7,
    'CY': 2,
    'CZ': 6,
}


def part_one(data) -> int:
    score = 0
    for i in data:
        i = i.replace(' ', '')
        score += SCORING[f'{i}']
    return score


def main():
    with open('day_two.txt', 'r') as f:
        data = f.read().splitlines()
    part_1 = part_one(data)
    # part_2 = part_two(data)

    print(f'Part One: {part_1}')
    # print(f'Part Two: {part_2}')


if __name__ == '__main__':
    main()
