

def main():
    with open('day_one.txt', 'r') as f:
        data = f.read().splitlines()
    part_1 = part_one(data)
    part_2 = part_two(data)

    print(f'Part One: {part_1}')
    print(f'Part Two: {part_2}')


if __name__ == '__main__':
    main()