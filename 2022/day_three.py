import string

sample_data = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw'
]


def part_one(data) -> int:
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


def part_two(data):
    groups = list(range(len(data) // 3))
    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    counting = list()

    for _ in groups:
        temp_list = data[:3]
        del data[:3]
        for i in temp_list[0]:
            if i in temp_list[1] and i in temp_list[2]:
                counting.append(alphabet.index(i) + 1)
                break

    return sum(counting)


def main():
    with open('day_three.txt', 'r') as f:
        data = f.read().splitlines()
    part_1 = part_one(data)
    part_2 = part_two(data)

    print(f'Part One: {part_1}')
    print(f'Part Two: {part_2}')


if __name__ == '__main__':
    main()
