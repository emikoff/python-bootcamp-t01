# Готово

import sys


def read_vectors():
    return list(map(float, sys.stdin.readline().split()))


def solve():
    vector1 = read_vectors()
    vector2 = read_vectors()

    return sum(a * b for a, b in zip(vector1, vector2))


if __name__ == "__main__":
    print(solve())
