from math import ceil, floor


def obtain_quadratic_result(a, b, c) -> int:
    return (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)


def obtain_vy_max(y) -> int:
    return (y ** 2 - y * 2) ** (1 / 2)


def propagate_y(vy_start, y_low, y_up):
    y_curr = vy_start * (vy_start + 1) / 2
    vy_curr = 0
    stop = False
    while not stop:
        y_curr -= vy_curr
        vy_curr += 1

        stop = y_up > y_curr >= y_low or y_curr < y_low

    return y_curr < y_low, y_up > y_curr >= y_low


if __name__ == '__main__':
    input_test = 'target area: x=20..30, y=-10..-5'
    x_min = 209
    x_max = 238
    y_min_targ = -59
    y_max_targ = -86
    vx_min = ceil(obtain_quadratic_result(1, 1, -2 * x_min))
    vx_max = floor(obtain_quadratic_result(1, 1, -2 * x_max))

    vy_max = round(obtain_vy_max(-y_max_targ))
    print(vy_max)
    y_max = vy_max * (vy_max + 1) / 2
    print(y_max)
    print(propagate_y(vy_max, y_max_targ, y_min_targ))
