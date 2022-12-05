import string

sample_data = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw'
]


def solve(data) -> int:
    counting = dict()
    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

    for line in data:
        half = int(len(line)/2)
        half1 = line[:half]
        for char in half1:
            if char in line[half:]:
                if counting.get(char) is None:
                    counting[char] = alphabet.index(char) + 1
                else:
                    counting[char] += alphabet.index(char) + 1
                break

    return sum(counting.values())


def main():
    with open('day_three.txt', 'r') as f:
        data = f.read().splitlines()
    part_1 = solve(data)
    # part_1, part_2 = solve(data)

    print(f'Part One: {part_1}')
    # print(f'Part Two: {part_2}')


if __name__ == '__main__':
    main()
