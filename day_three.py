from statistics import mode
from collections import Counter


def _config() -> list:
    with open('data_day3.txt', 'r') as data:
        instructions = [f'0o{line}' for line in data.read().splitlines()]

    return instructions


def do_stuff(data):
    gamma = ''
    epsilon = ''
    loop = 0
    finish = len(data[0][2:])
    oxygen = {n: [] for n in range(finish)}  # common and 1
    co2 = {n: [] for n in range(finish)}  # uncommon and 0

    while loop != finish:
        current_bin = []
        for number in data:
            bit = number[2:][loop]
            current_bin.append(bit)
        gamma += mode(current_bin)
        epsilon += Counter(current_bin).most_common()[-1][0]

        compare = Counter(current_bin)
        oxygen_value = '0' if compare['0'] >= compare['1'] else '1'
        co2_value = '0' if compare['0'] <= compare['1'] else '1'
        # for i in data:
        #     if i[2:].startswith(oxygen_value):
        #         if oxygen[loop]:
        #             if len(oxygen[loop]) != finish:
        #                 oxygen[loop] = i
        #         else:
        #             oxygen[loop] = i
        #     elif len(co2[loop]) != finish:
        #         co2[loop] = i
        oxygen[loop] = [i for i in data if i[2:].startswith(oxygen_value) and len(oxygen[loop]) != finish]
        co2[loop] = [i for i in data if i[2:].startswith(co2_value) and len(oxygen[loop]) != finish]

        loop += 1

    print(oxygen, '\n', co2)

    return int(gamma, 2) * int(epsilon, 2), True


def main():
    data = [
        '0o00100', '0o11110', '0o10110', '0o10111', '0o10101', '0o01111', '0o00111', '0o11100', '0o10000', '0o11001',
        '0o00010', '0o01010'
    ]

    # data = _config()
    result_one, result_two = do_stuff(data)
    print(f'Part one: {result_one}')
    print(f'Part two: {result_two}')


if __name__ == '__main__':
    main()
