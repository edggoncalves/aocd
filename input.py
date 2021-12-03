import aocd
from os import path


def config(day, year):
    base_path = path.dirname(__file__)
    relative_path = 'token'
    token_path = path.join(base_path, relative_path)
    token = open(token_path, 'r').read()
    data = aocd.get_data(token, day=day, year=year)

    return data


print(config(2, 2021))
