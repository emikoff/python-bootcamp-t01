def read_devices_by_year(n):
    devices_by_year = {}

    for _ in range(n):
        try:
            year, cost, work_time = [int(el) for el in input().split()]
        except ValueError:
            error()
        if year not in devices_by_year:
            devices_by_year[year] = []
        devices_by_year[year].append((cost, work_time))

    return devices_by_year


def filter_candidate_years(devices_by_year):
    candidates_by_year = {}
    for year in devices_by_year:
        if len(devices_by_year[year]) >= 2:
            candidates_by_year[year] = devices_by_year[year]

    return candidates_by_year


def min_cost(candidates_by_year, target_work_time):
    total_costs = []

    for year in candidates_by_year:
        arr = candidates_by_year[year]
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                cost = arr[i][0] + arr[j][0]
                work_time = arr[i][1] + arr[j][1]
                if work_time == target_work_time:
                    total_costs.append(cost)
    return min(total_costs)


def error():
    print("Incorrect input")
    raise SystemExit


def main():
    try:
        n, target_work_time = [int(el) for el in input().split()]
    except ValueError:
        error()

    devices_by_year = read_devices_by_year(n)
    candidates_by_year = filter_candidate_years(devices_by_year)
    print(min_cost(candidates_by_year, target_work_time))


if __name__ == "__main__":
    main()
