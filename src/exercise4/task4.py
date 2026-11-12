def main():
    try:
        triangle = []
        current_row = [1]

        rows_count = int(input())
        if rows_count <= 0:
            raise ValueError

        for _ in range(rows_count - 1):
            triangle.append(current_row)
            inner_values = []
            if len(current_row) > 1:
                inner_values = [sum(current_row[i : i + 2]) for i in range(len(current_row) - 1)]
            current_row = [1] + inner_values + [1]

        triangle.append(current_row)

        for row in triangle:
            print(*row)
    except ValueError:
        print("Natural number was expected")

if __name__ == "__main__":
    main()
