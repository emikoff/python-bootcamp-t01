import sys


def calculate_best_cell_value(row: int, column: int, matrix: list[list[int]]) -> int:
    if row == 0 and column == 0:
        return matrix[row][column]

    if row == 0:
        return matrix[row][column] + matrix[row][column - 1]

    if column == 0:
        return matrix[row][column] + matrix[row - 1][column]

    return matrix[row][column] + max(matrix[row - 1][column], matrix[row][column - 1])


def read_matrix() -> tuple[list, int, int]:
    rows_count, cols_count = map(int, sys.stdin.readline().split())
    matrix = []
    for _ in range(rows_count):
        matrix.append(list(map(int, sys.stdin.readline().split())))

    return matrix, rows_count, cols_count


def calculate_max_coins_matrix(
    matrix: tuple[list, int, int], rows_count: int, cols_count: int
) -> tuple[list, int, int]:
    for row in range(rows_count):
        for col in range(cols_count):
            matrix[row][col] = calculate_best_cell_value(row, col, matrix)

    return matrix


def main() -> None:
    matrix, rows_count, cols_count = read_matrix()
    max_coins_matrix = calculate_max_coins_matrix(
        [x.copy() for x in matrix.copy()], rows_count, cols_count
    )
    print(max_coins_matrix[-1][-1])


if __name__ == "__main__":
    main()
