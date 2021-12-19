def part2(crabs):
    result = [0] * max(crabs)
    for idx, fuel in enumerate(result):
        result[idx] = sum([abs(x - idx) * (abs(x - idx) + 1) // 2 for x in crabs])
    return result


if __name__ == '__main__':
    with open("../data/day7.txt") as file:
        input_data = file.read()
        data = [int(i) for i in input_data.split(',')]
        result = [0] * max(data)

        for idx, fuel in enumerate(result):
            result[idx] = sum([abs(x - idx) for x in data])
        print(min(result))

        print(min(part2(data)))
