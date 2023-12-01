import re


def get_data():
    # with open("sample.txt", "r") as f:
    with open("day_five.txt", "r") as f:
        input_data = f.read().splitlines()
    return input_data


def separate_boxes_from_instructions(input_data: list) -> tuple[list[str], int, list[str]]:
    stacks = list()
    for _ in input_data:
        boxes = input_data.pop(0)
        if boxes:
            stacks.append(boxes)
        else:
            break
    instructions = input_data
    columns = len(stacks.pop(-1).split())
    return stacks, columns, instructions


def parse_instructions(instructions: list[str]) -> list[dict[str:str]]:
    parsed_instructions = list()
    for instruction in instructions:
        quantity, from_stack, to_stack = re.findall(string=instruction, pattern=r"\d+")
        parsed_instructions.append(
            {
                "quantity": quantity,
                "from_stack": from_stack,
                "to_stack": to_stack,
            }
        )
    return parsed_instructions


def separate_stacks(stacks: list[str], columns: int) -> dict[str:list[str]]:
    separated_stacks = {f"{column + 1}": [] for column in range(columns)}
    for line in stacks:
        n = 0
        boxes = line[1::4]
        for box in boxes:
            n += 1
            if box.strip():
                separated_stacks[f"{n}"].append(box)
    return separated_stacks


def move_boxes(
        parsed_instructions: list[dict[str:str]],
        separated_stacks: dict[str:list[str]]
) -> dict[str:list[str]]:
    for instruction in parsed_instructions:
        quantity = int(instruction["quantity"])
        from_stack = instruction["from_stack"]
        to_stack = instruction["to_stack"]
        to_move = separated_stacks[f"{from_stack}"][:quantity]
        separated_stacks[f"{from_stack}"] = separated_stacks[f"{from_stack}"][quantity:]
        for box in to_move:
            separated_stacks[f"{to_stack}"].insert(0, box)
    return separated_stacks


def part_one(input_data: list[str]):
    stacks, columns, instructions = separate_boxes_from_instructions(input_data=input_data)
    parsed_instructions = parse_instructions(instructions=instructions)
    separated_stacks = separate_stacks(stacks=stacks, columns=columns)
    moved_boxes = move_boxes(parsed_instructions=parsed_instructions, separated_stacks=separated_stacks)
    top_row = "".join([moved_boxes[f"{column}"][0] for column in moved_boxes])
    print(top_row)


if __name__ == "__main__":
    data: list[str] = get_data()
    part_one(data)
