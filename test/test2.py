from collections import Counter


def solution(a):
    numbers = list(set(a))
    maximum = 200000
    moves = 0
    sorted_a = sorted(a)

    count = Counter(sorted_a)
    for k, v in count.items():
        internal_moves = 0
        if v > 1:
            increased = k + 1
            decreased = k - 1
            while len(sorted_a) != len(numbers):
                if increased not in numbers and increased > maximum:
                    internal_moves += 1
                    sorted_a.append(increased)
                elif decreased not in numbers:
                    internal_moves += 1
                    sorted_a.append(decreased)
                internal_moves += 1
                # v -= 1

        moves += internal_moves
        return moves

    # return 1


list_ = [1, 2, 1]
# a = [2, 1, 4, 4]
# a = [6, 2, 1, 5, 4, 3]
print(solution(list_))
