def main() -> None:
    degree, x = input().split()
    degree = int(degree)
    x = float(x)

    coefficients = [float(input()) for _ in range(degree + 1)]

    derivative = 0
    for i in range(len(coefficients) - 1):
        degree = degree - i
        derivative += coefficients[i] * degree * x ** (degree - 1)

    print(f"{derivative:.3f}")


if __name__ == "__main__":
    main()
