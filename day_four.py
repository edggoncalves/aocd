def _config() -> tuple:
    # with open('data_day4.txt', 'r') as data:
    with open('sample_data_day4.txt', 'r') as data:
        instructions = [line for line in data.read().splitlines()]

    numbers = instructions.pop(0)
    board = 0
    boards = {board: []}
    for line in instructions:
        if line:
            boards[board].append(line.strip().split())
        else:
            board += 1
            boards[board] = []

    return numbers, boards


def part_one(numbers, boards) -> str:
    player = 1
    for board in list(range(len(boards))):
        scoreboard = Board(board, player)
        winner = scoreboard.check_score(numbers)

        return winner


class Board:
    def __init__(self, board, player):
        lines = len(board)
        columns = len(board[0])

    def check_score(self, number):
        self.horizontal()
        self.vertical()

        return 'winner'

    def score_point(self):

        pass

    def horizontal(self):
        pass

    def vertical(self):
        pass


def main():
    numbers, boards = _config()
    result_one = part_one(numbers, boards)
    # result_two = part_two(data)
    print(f'Part one: {result_one}')
    # print(f'Part two: {result_two}')


if __name__ == '__main__':
    main()
