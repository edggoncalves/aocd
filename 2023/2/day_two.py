from input import get_data
import re

CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def _parse_game_cubes(input_data: list[str]) -> tuple[list[int], list[int]]:
    possible_games = []
    impossible_games = []
    for line in input_data:
        game = re.search(r"Game (\d+):", line).group(1)
        possible = []
        draws = line.split(";")
        for draw in draws:
            red_cubes = sum(int(cube) for cube in re.findall(r"(\d+) red", draw))
            green_cubes = sum(int(cube) for cube in re.findall(r"(\d+) green", draw))
            blue_cubes = sum(int(cube) for cube in re.findall(r"(\d+) blue", draw))
            if red_cubes <= CUBES["red"] and green_cubes <= CUBES["green"] and blue_cubes <= CUBES["blue"]:
                possible.append(True)
            else:
                possible.append(False)
        if all(possible):
            possible_games.append(int(game))
        else:
            impossible_games.append(int(game))
    return possible_games, impossible_games


def _power_minimum(input_data: list[str]) -> int:
    power = 0
    for line in input_data:
        min_red = max(int(red) for red in re.findall(r"(\d+) red", line))
        min_green = max(int(green) for green in re.findall(r"(\d+) green", line))
        min_blue = max(int(blue) for blue in re.findall(r"(\d+) blue", line))
        power += (int(min_red) * int(min_green) * int(min_blue))
    return power


def part_one(input_data: list[str]):
    possible_games, impossible_games = _parse_game_cubes(input_data)
    return sum(possible_games)


def part_two(input_data: list[str]):
    power = _power_minimum(input_data)
    return power


if __name__ == "__main__":
    data = get_data(year="2023", day="2", input_data="day_two")
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")
