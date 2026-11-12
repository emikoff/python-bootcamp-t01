def dfs(
    row: int,
    col: int,
    rows_count: int,
    cols_count: int,
    matrix: list[list[int]],
    figure: list[tuple[int, int]],
) -> None:
    """
    Обходит фигуру методом DFS и сохраняет координаты её клеток.
    """

    if row < 0 or row >= rows_count or col < 0 or col >= cols_count:
        return

    if matrix[row][col] != 1:
        return

    matrix[row][col] = 0
    figure.append((row, col))

    dfs(row + 1, col, rows_count, cols_count, matrix, figure)
    dfs(row - 1, col, rows_count, cols_count, matrix, figure)
    dfs(row, col + 1, rows_count, cols_count, matrix, figure)
    dfs(row, col - 1, rows_count, cols_count, matrix, figure)


def get_bounding_rectangle_area(figure: list[tuple[int, int]]) -> int:
    """
    Вычисляет площадь ограничивающего прямоугольника фигуры.
    """
    rows = [row for row, col in figure]
    cols = [col for row, col in figure]

    height = max(rows) - min(rows) + 1
    width = max(cols) - min(cols) + 1

    return height * width


def load_matrix() -> list[list[int]]:
    """
    Загружает матрицу из файла input.txt.
    """
    with open("input.txt", encoding="utf-8") as file:
        return [list(map(int, line.split())) for line in file]


def main() -> None:
    matrix = load_matrix()

    rows_count = len(matrix)
    cols_count = len(matrix[0])

    square_count = 0
    circle_count = 0

    for row in range(rows_count):
        for col in range(cols_count):
            figure: list[tuple[int, int]] = []
            dfs(row, col, rows_count, cols_count, matrix, figure)

            if figure:
                is_square = len(figure) == get_bounding_rectangle_area(figure)

                if is_square:
                    square_count += 1
                else:
                    circle_count += 1

    print(square_count, circle_count)


if __name__ == "__main__":
    main()
