import aocd
from os import path


def config(day, year):
    base_path = path.dirname(__file__)
    relative_path = "token"
    token_path = path.join(base_path, relative_path)
    with open(token_path, "r") as f:
        token = f.read()
    data = aocd.get_data(token, day=int(day), year=int(year))

    return data


def get_data(input_data: str, year: str, day: str) -> list[str]:
    base_path = path.dirname(__file__)
    with open(f"{path.join(base_path, year, day, input_data)}.txt", "r") as f:
        output_data = f.read().splitlines()
    return output_data


def get_input(day: str, year: str):
    base_path = path.dirname(__file__)
    relative_path = "data"
    data_path = path.join(base_path, year, day, f"{relative_path}.txt")
    if not path.exists(data_path):
        data = config(day, year)
        with open(data_path, "w") as f:
            f.write(data)
    else:
        print("Data already exists")
