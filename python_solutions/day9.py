import copy
from typing import List, Tuple


def get_array_data(read_data: List[str]) -> List[List[int]]:
    result = []
    for line in read_data:
        result.append([int(i) for i in line])
    return result


def get_list_lowest_points(height_map: List[List[int]]) -> List[Tuple[int, int, int]]:
    result = []

    for idy in range(len(height_map)):
        for idx in range(len(height_map[0])):
            is_lowest = True
            if idx == 0:
                is_lowest = is_lowest and height_map[idy][idx] < height_map[idy][idx + 1]
            elif idx == len(height_map[0]) - 1:
                is_lowest = is_lowest and height_map[idy][idx] < height_map[idy][idx - 1]
            else:
                is_lowest = is_lowest and height_map[idy][idx] < height_map[idy][idx + 1] and height_map[idy][idx] < \
                            height_map[idy][idx - 1]

            if idy == 0:
                is_lowest = is_lowest and height_map[idy][idx] < height_map[idy + 1][idx]
            elif idy == len(height_map) - 1:
                is_lowest = is_lowest and height_map[idy][idx] < height_map[idy - 1][idx]
            else:
                is_lowest = is_lowest and height_map[idy][idx] < height_map[idy + 1][idx] and height_map[idy][idx] < \
                            height_map[idy - 1][idx]

            if is_lowest:
                result.append((height_map[idy][idx], idy, idx))

    return result


def get_basin_size(height_map: List[List[int]], idy: int, idx: int, can_up=False, can_down=False) -> List[Tuple[int, int]]:
    result = []
    keep_counting = True
    count_x = copy.deepcopy(idx)
    count_y = copy.deepcopy(idy)
    max_y = len(height_map) - 1
    max_x = len(height_map[0]) - 1

    while keep_counting:
        # count to left
        if count_x >= 0 and height_map[count_y][count_x] < 9:
            result.append((count_y, count_x))
            if count_y < max_y and height_map[idy + 1][count_x] < 9 and can_down:
                result.extend(get_basin_size(height_map, idy + 1, count_x, can_down=True))
            if count_y > 0 and height_map[idy - 1][count_x] < 9 and can_up:
                result.extend(get_basin_size(height_map, idy - 1, count_x, can_up=True))
            count_x -= 1
        else:
            keep_counting = False

    keep_counting = True
    count_x = copy.deepcopy(idx)
    count_y = copy.deepcopy(idy)
    while keep_counting:
        # count to right
        if count_x <= max_x and height_map[count_y][count_x] < 9:
            result.append((count_y, count_x))
            if count_y < max_y and height_map[idy + 1][count_x] < 9 and can_down:
                result.extend(get_basin_size(height_map, idy + 1, count_x, can_down=True))
            if count_y > 0 and height_map[idy - 1][count_x] < 9 and can_up:
                result.extend(get_basin_size(height_map, idy - 1, count_x, can_up=True))

            count_x += 1

        else:
            keep_counting = False

    return result


def get_risk(heights: List[Tuple[int, int, int]]) -> int:
    return sum([val + 1 for val, idy, idx in heights])


if __name__ == '__main__':
    with open("../data/day9.txt") as file:
        data = file.read().splitlines()
        array_in = get_array_data(data)
        lowest_points = get_list_lowest_points(array_in)
        res = []
        for value, idy, idx in lowest_points:
            res.append(len(set(get_basin_size(array_in, idy, idx, True, True))))

        res.sort(reverse=True)
        final = 1
        for n in res[:3]:
            final *= n
        print(final)
