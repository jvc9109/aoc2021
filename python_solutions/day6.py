def count_fish(data, days):
    tracker = [data.count(i) for i in range(9)]
    for day in range(days):
        tracker[(day + 7) % 9] += tracker[day % 9]
    return sum(tracker)


if __name__ == '__main__':
    with open("./data/day6.txt") as file:
        input_data = file.read()
        data = [int(i) for i in input_data.split(',')]

        print(count_fish(data,80))
        print(count_fish(data,256))
