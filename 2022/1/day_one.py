# sample_data = ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000']


def sum_cals(data: list) -> list:
    elf = 1
    elves = {
        elf: 0
    }
    for i in data:
        if len(i) > 0:
            elves[elf] = elves[elf] + int(i)
        else:
            elf += 1
            elves[elf] = 0

    return [elves[elf] for elf in elves]


def part_one(data: list) -> int:
    elves = sum_cals(data)

    return max(elves)


def part_two(data):
    elves = sum_cals(data)

    elves.sort()

    return sum(elves[-3:])


def main():
    with open('day_one.txt', 'r') as f:
        data = f.read().splitlines()
    part_1 = part_one(data)
    part_2 = part_two(data)

    print(f'Part One: {part_1}')
    print(f'Part Two: {part_2}')


if __name__ == '__main__':
    main()
