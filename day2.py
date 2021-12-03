def calculate_position(instructions: list) -> tuple:
    h = 0
    d = 0

    for instruction in instructions:
        direction, steps = instruction.split()
        if direction == 'forward':
            h += int(steps)
        elif direction == 'down':
            d += int(steps)
        elif direction == 'up':
            d -= int(steps)

    return h, d


def calculate_position_with_aim(instructions: list) -> tuple:
    h = 0
    d = 0
    aim = 0

    for instruction in instructions:
        direction, steps = instruction.split()
        if direction == 'forward':
            h += int(steps)
            d += aim * int(steps)
        elif direction == 'down':
            aim += int(steps)
        elif direction == 'up':
            aim -= int(steps)

    return h, d


if __name__ == '__main__':
    with open("./data/day2.txt") as file:
        data = file.read().splitlines()
        horizontal, depth = calculate_position(data)
        print(horizontal * depth)
        horizontal, depth = calculate_position_with_aim(data)
        print(horizontal * depth)
