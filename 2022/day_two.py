# sample_data = {
#     'A': 'Y',
#     'B': 'X',
#     'C': 'Z'
# }

SCORING_1 = {'AX': 4, 'AY': 8, 'AZ': 3, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 7, 'CY': 2, 'CZ': 6}
SCORING_2 = {'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}


def solve(data) -> tuple:
    score_1 = 0
    score_2 = 0
    for i in data:
        i = i.replace(' ', '')
        score_1 += SCORING_1[i]
        score_2 += SCORING_2[i]
    return score_1, score_2


def main():
    with open('day_two.txt', 'r') as f:
        data = f.read().splitlines()
    part_1, part_2 = solve(data)

    print(f'Part One: {part_1}')
    print(f'Part Two: {part_2}')


if __name__ == '__main__':
    main()
