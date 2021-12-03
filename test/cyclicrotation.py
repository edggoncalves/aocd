import numpy as np


def rotate(k, rotated) -> list:
    if k == 0:
        return rotated
    else:
        i = rotated.pop(0)
        k -= 1
        rotated.append(i)
        return rotate(k, rotated)


def solution(n, k):
    rotated = [i for i in n]
    rotated = rotate(k, rotated)
    print(f'Before: {n}')
    print(f'Multiplier : {k}')
    print(f'After: {rotated}')


list_ = np.random.randint(1, 11, 5)
multiplier = np.random.randint(1, 11, 1)[0]
solution(list_, multiplier)
