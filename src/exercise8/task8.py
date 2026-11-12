def main() -> None:
    numbers_count = int(input())

    unique_numbers = {int(input()) for _ in range(numbers_count)}

    print(len(unique_numbers))


if __name__ == "__main__":
    main()
