def split_and_validate(data: str):
    """Проверяет корректность данных и возвращает знак, целую и дробную части."""
    sign = ""
    integer_part = data
    fractional_part = "0"

    if not data:
        return None

    if data[0] in "+-":
        sign = data[0]
        data = data[1:]

        if not data:
            return None

    if data.count(".") > 1:
        return None

    if "." in data:
        parts = data.split(".")

        if len(parts) != 2:
            return None

        integer_part, fractional_part = parts

        if not integer_part or not fractional_part:
            return None
    else:
        integer_part = data

    if not integer_part.isdigit() or not fractional_part.isdigit():
        return None

    return sign, integer_part, fractional_part


def multiply_by_two(parsed_data):
    """Умножает число на 2 и возвращает результат с тремя знаками после точки."""
    if parsed_data is None:
        return "Incorrect input"

    sign, integer_part, fractional_part = parsed_data

    fraction_length = len(fractional_part)
    multiplier = 10**fraction_length

    number = int(integer_part + fractional_part)
    result = number * 2

    result_integer_part = result // multiplier
    result_fractional_part = result % multiplier

    result_fractional_part = str(result_fractional_part).zfill(fraction_length)

    # Доводим дробную часть ровно до 3 знаков
    if len(result_fractional_part) < 3:
        result_fractional_part += "0" * (3 - len(result_fractional_part))
    else:
        result_fractional_part = result_fractional_part[:3]

    result = f"{result_integer_part}.{result_fractional_part}"

    if sign == "-":
        return f"-{result}"

    return result


if __name__ == "__main__":
    data = input()
    parsed_data = split_and_validate(data)
    print(multiply_by_two(parsed_data))
