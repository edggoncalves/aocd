from statistics import mode
from collections import Counter


def _config() -> list:
    with open('data_day3.txt', 'r') as data:
        instructions = [f'0o{line}' for line in data.read().splitlines()]

    return instructions


def part_one(data):
    gamma = ''
    epsilon = ''
    loop = 0
    finish = len(data[0][2:])

    while loop != finish:
        current_bin = []
        for number in data:
            bit = number[2:][loop]
            current_bin.append(bit)
        gamma += mode(current_bin)
        epsilon += Counter(current_bin).most_common()[-1][0]

        loop += 1

    return int(gamma, 2) * int(epsilon, 2)


def most_least_common(list_: list, start: int, gas_name: str) -> str:
    count = Counter([i[2:][start] for i in list_])
    oxygen = '1' if count['1'] >= count['0'] else '0'
    co2 = '1' if count['1'] <= count['0'] else '0'

    return oxygen if gas_name == 'oxygen' else co2


def part_two(data: list):
    start = 0
    oxygen = {'name': 'oxygen', 'value': []}  # common and 1
    co2 = {'name': 'co2', 'value': []}  # uncommon and 0

    for gas in [oxygen, co2]:
        new_gas = {'name': gas['name'], 'value': data[:]}
        while len(gas) != 1:
            gas = {'name': gas['name'], 'value': []}
            bit = most_least_common(new_gas['value'], start, gas['name'])
            for binary in new_gas['value']:
                if binary[2:][start].startswith(bit):
                    gas['value'].append(binary)
            new_gas = gas.copy()
            if len(new_gas['value']) == 1:
                oxygen['value'].append(new_gas['value'][0]) if new_gas['name'] == 'oxygen' \
                    else co2['value'].append(new_gas['value'][0])
            start += 1

    print(co2, '\n', oxygen)
    # while len(co2) != 1:
    #     co2 = []
    #     bit = least_common(new_gas, start)
    #     for binary in new_gas:
    #         if binary[2:][start].startswith(bit):
    #             co2.append(binary)
    #     new_gas = co2[:]
    #     start += 1
    #
    # return True


def main():
    data = [
        '0o00100', '0o11110', '0o10110', '0o10111', '0o10101', '0o01111', '0o00111', '0o11100', '0o10000', '0o11001',
        '0o00010', '0o01010'
    ]

    # data = _config()
    result_one = part_one(data)
    result_two = part_two(data)
    print(f'Part one: {result_one}')
    print(f'Part two: {result_two}')


if __name__ == '__main__':
    main()
