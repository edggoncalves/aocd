example_data = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb", 
                "bvwbjplbgvbhsrlpgdmjqwftvncz", 
                "nppdvjthqldpwncqszvftbrmjlhg",
                "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
                "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]

def example(example_data):
    for i in example_data:
        axis_x = 0
        axis_y = 4
        for j in i:
            slice = i[axis_x:axis_y]
            """Find unique letters in slice"""
            if len(set(slice)) != 4:
                axis_x += 1
                axis_y += 1
            else:
                print(slice)
                print(f"Signal is {axis_y}")
                break

example(example_data)


def get_data():
    with open("day_six.txt", "r") as f:
        data = f.read().splitlines()
    return data


def part_one(data):
    for i in data:
        axis_x = 0
        axis_y = 4
        for j in i:
            slice = i[axis_x:axis_y]
            """Find unique letters in slice"""
            if len(set(slice)) != 4:
                axis_x += 1
                axis_y += 1
            else:
                print(slice)
                print(f"Signal is {axis_y}")
                break


def part_two(data):
    for i in data:
        axis_x = 0
        axis_y = 14
        for j in i:
            slice = i[axis_x:axis_y]
            """Find unique letters in slice"""
            if len(set(slice)) != 14:
                axis_x += 1
                axis_y += 1
            else:
                print(slice)
                print(f"Signal is {axis_y}")
                break


def test(data: list[str]):
    """find unique 14 letter sequence in string"""
    


if __name__ == "__main__":
    data = get_data()
    part_one(data)
    part_two(data)
