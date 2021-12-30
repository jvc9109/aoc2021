from math import ceil, floor


def obtain_quadratic_result(a, b, c) -> int:
    return (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)


def obtain_vy_max(y) -> int:
    return (y ** 2 - y * 2) ** (1 / 2)


def propagate(vx, vy, y_low, y_up, x_low, x_high):
    stop = False
    y_curr = 0
    x_curr = 0
    matched = False
    while not stop:
        y_curr += vy
        x_curr += vx
        vx = vx - 1 if vx > 0 else vx + 1 if vx < 0 else 0
        vy -= 1
        missed = x_curr > x_high or y_curr < y_low
        matched = x_low <= x_curr <= x_high and y_up >= y_curr >= y_low
        stop = missed or matched

    return matched


def solve(x_mi, x_ma, y_mi, y_ma):
    vx_min = ceil(obtain_quadratic_result(1, 1, -2 * x_mi))
    vx_max = floor(obtain_quadratic_result(1, 1, -2 * x_ma))

    vy_max = round(obtain_vy_max(-y_ma))
    y_max = vy_max * (vy_max + 1) / 2
    print(f'maximum hight {y_max}')
    combinations = set()

    for i in range(x_mi, x_ma + 1):
        for j in range(y_ma, y_mi + 1):
            combinations.add((i, j))

    for ix in range(vx_min, x_ma + 1):
        for iy in range(vy_max, y_ma - 1, -1):
            if propagate(ix, iy, y_ma, y_mi, x_mi, x_ma):
                combinations.add((ix, iy))

    print(f'total combinations {len(combinations)}')

    return int(y_max), len(combinations)


if __name__ == '__main__':
    max_height_test, comb_test = solve(20, 30, -5, -10)
    assert max_height_test == 45
    assert comb_test == 112

    solve(209, 238, -59, -86)
