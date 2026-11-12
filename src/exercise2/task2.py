def reverse_num(num):
    result = 0

    while num > 0:
        result *= 10
        result += num % 10
        num //= 10

    return result


def is_palindrom():
    num = int(input())
    return num == reverse_num(num)


if __name__ == "__main__":
    print(is_palindrom())
