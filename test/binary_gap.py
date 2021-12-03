import random


def _convert(n) -> list:
    return [int(x) for x in str(bin(n)[2:])]


def highest(binary, position_one, count=0, index=1) -> int:
    for i in position_one[:-1]:
        end = position_one[index]
        new_count = len(binary[i:end]) - 1
        if new_count > count:
            count = new_count
        index += 1

    return count


def solution(n):
    binary = _convert(n)
    position_one = []

    for i in range(len(binary)):
        if binary[i] == 1:
            position_one.append(i)

    count = highest(binary, position_one)

    print(f'{n} -> {binary}\n{count}')


def solution2(n):
    print(len(max(bin(n)[2:].strip('0').split('1'))))


n = random.randrange(1, 100000000)
solution(n)
solution2(n)
