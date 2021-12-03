import input


def count_increases(numbers):
    count = 0
    a = 1
    b = 0
    for number in range(len(numbers)):
        try:
            if numbers[a] > numbers[b]:
                count += 1
            a += 1
            b += 1
        except IndexError:
            return count


def times3(numbers):
    count = 0
    index = 0

    for number in numbers[1:-2]:
        a = numbers[index]
        b = numbers[index + 1]
        c = numbers[index + 2]
        d = numbers[index + 3]
        if b + c + d > a + b + c:
            count += 1
        index += 1

    return count


def main():
    data = input.config(day=1, year=2021)
    numbers = [int(number) for number in data.splitlines()]

    increases = count_increases(numbers)
    increments_of_3 = times3(numbers)

    print(f'Part 1: {increases}')
    print(f'Part 2: {increments_of_3}')


if __name__ == '__main__':
    main()
