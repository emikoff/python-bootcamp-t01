import json


def exit_with_error():
    print("Incorrect json")
    raise SystemExit


def validate_movies(movies):
    if not isinstance(movies, list):
        exit_with_error()
    for movie in movies:
        if not isinstance(movie, dict):
            exit_with_error()
        if "title" not in movie or "year" not in movie:
            exit_with_error()
        if not isinstance(movie["title"], str) or not isinstance(movie["year"], int):
            exit_with_error()

    years = [movie["year"] for movie in movies]
    if years != sorted(years):
        exit_with_error()


def load_data(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read().strip()
        if not text:
            print("Empty file")
            raise SystemExit

        data = json.loads(text)
        if not isinstance(data, dict):
            exit_with_error()
        return data
    except SystemExit:
        raise
    except ValueError:
        exit_with_error()
    except FileNotFoundError:
        print("File not found")
        raise SystemExit


def main(path):
    data = load_data(path)

    if "list1" not in data or "list2" not in data:
        exit_with_error()

    merged_movies = []
    for value in (data["list1"], data["list2"]):
        validate_movies(value)
        merged_movies.extend(value)

    result = sorted(merged_movies, key=lambda x: x["year"])
    return json.dumps({"list0": result}, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    print(main("input.txt"))
