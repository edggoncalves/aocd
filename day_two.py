def _config() -> list:
    with open('data_day2.txt', 'r') as data:
        instructions = [line for line in data.read().splitlines()]

    return instructions


def make_dict(instructions) -> dict:
    forward = 0
    up = 0
    down = 0
    for instruction in instructions:
        direction, value = instruction.split(' ')
        if direction == 'forward':
            forward += int(value)
        elif direction == 'up':
            up += int(value)
        else:
            down += int(value)

    instructions = {
        'forward': forward,
        'up': up,
        'down': down
    }

    return instructions


def make_dict_part_two(instructions) -> dict:
    directions = {
        'up': 0,
        'down': 0,
        'forward': 0,
        'aim': 0
    }

    for instruction in instructions:
        direction, value = instruction.split(' ')
        if direction == 'forward':
            if directions['aim'] <= 0:
                directions['forward'] += int(value)
            else:
                directions['forward'] += int(value)
                directions['down'] += int(value) * directions['aim']
        elif direction == 'up':
            directions['aim'] -= int(value)
        elif direction == 'down':
            directions['aim'] += int(value)

    return directions


def part_one(instructions) -> int:
    directions = make_dict(instructions)
    result = directions['forward'] * (directions['down'] - directions['up'])

    return result


def part_two(instructions) -> int:
    directions = make_dict_part_two(instructions)
    result = directions['forward'] * directions['down']

    return result


def main():
    instructions = _config()
    # instructions = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

    output = part_one(instructions)
    output2 = part_two(instructions)
    print(f'Part one: {output}')
    print(f'Part two: {output2}')


if __name__ == '__main__':
    main()
