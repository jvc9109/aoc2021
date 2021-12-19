def get_how_much_increase(depths: list) -> int:
    count = 0
    previous_depth = int(depths[0])
    for depth in depths[1:]:
        if int(depth) > previous_depth:
            count += 1
        previous_depth = int(depth)
    return count


def get_how_much_increases_with_sliding(depths: list) -> int:
    sum_depths = []
    for i in range(len(depths) - 2):
        sum_depths.append(sum([int(el) for el in depths[i:i+3]]))
    return get_how_much_increase(sum_depths)


if __name__ == '__main__':
    with open("../data/day1.txt") as file:
        data = file.read().splitlines()
        print(get_how_much_increase(data))
        print(get_how_much_increases_with_sliding(data))
