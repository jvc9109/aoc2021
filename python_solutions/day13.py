from __future__ import annotations

from typing import List, Tuple


class Dot:
    x: int
    y: int

    def __init__(self, x_position: int, y_position: int) -> None:
        self.x = x_position
        self.y = y_position

    def __eq__(self, other: Dot) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def translate_y(self, axis) -> None:
        if self.y < axis:
            return
        distances_to_axis = self.y - axis
        self.y = axis - distances_to_axis

    def translate_x(self, axis) -> None:
        if self.x < axis:
            return
        distance = self.x - axis
        self.x = axis - distance


def build_dots(data: List[str]) -> Tuple[List[Dot], List[Tuple[str, int]]]:
    list_coords = []
    folds = []

    for coord_dot in data:
        if coord_dot == '':
            continue

        if 'fold' in coord_dot:
            position = int(coord_dot.split('=')[1])
            axis = coord_dot.split('=')[0][-1]
            folds.append((axis, position))
            continue
        x, y = [int(i) for i in coord_dot.split(',')]
        list_coords.append(Dot(x, y))
    return list_coords, folds


def make_folds(dots: List[Dot], folds: List[Tuple[str, int]]) -> List[Dot]:
    for axis, position in folds:
        if axis == 'x':
            for dot in dots:
                dot.translate_x(position)
        elif axis == 'y':
            for dot in dots:
                dot.translate_y(position)
        dots = list(set(dots))

    return dots


def print_dots(dots: List[Dot]) -> None:
    mosaic = []
    for y in range(6):
        mosaic.append(['.' for i in range(40)])

    for dot in dots:
        mosaic[dot.y][dot.x] = '#'

    for y in mosaic:
        print(''.join(y))


if __name__ == '__main__':
    input_test = '6,10\n0,14\n9,10\n0,3\n10,4\n4,11\n6,0\n6,12\n4,1\n0,13\n10,12\n3,4\n3,0\n8,4\n1,10\n2,14\n8,10\n9,0'
    input_test += '\n\nfold along y=7\nfold along x=5'
    data = input_test.splitlines()
    dots_list, instrucctions = build_dots(data)

    result = make_folds(dots_list, [instrucctions[0]])

    assert (len(result) == 17)
    with open("../data/day13.txt") as file:
        data = file.read().splitlines()
        dots_list, instrucctions = build_dots(data)

        result = make_folds(dots_list, instrucctions)
        print(len(result))
        print_dots(result)
