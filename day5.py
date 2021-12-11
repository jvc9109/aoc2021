from typing import List


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class VectorLine:
    origin: Point
    final: Point
    is_flat: bool

    def __init__(self, origin: Point, final: Point) -> None:
        self.origin = origin
        self.final = final
        self.is_flat = self.get_is_flat()

    def get_is_flat(self) -> bool:
        return self.origin.x == self.final.x or self.origin.y == self.final.y


def create_vectors(data: List[str]) -> List[VectorLine]:
    result = []
    for line in data:
        origin_points, final_points = line.split(' -> ')
        x1, y1 = [int(i) for i in origin_points.split(',')]
        x2, y2 = [int(i) for i in final_points.split(',')]
        result.append(VectorLine(Point(x1, y1), Point(x2, y2)))

    return result


class VentMap:
    map: List[List[int]]
    x_limit: int
    y_limit: int
    crossing_count: int

    def __init__(self) -> None:
        self.map = [[0]]
        self.crossing_count = 0
        self.x_limit = 0
        self.y_limit = 0

    def update_y_limit(self, new_limit: int):
        if new_limit > self.y_limit:
            for idy in range(new_limit - self.y_limit):
                self.map.append([0] * (self.x_limit + 1))
            self.y_limit = new_limit

    def update_x_limit(self, new_limit: int):
        if new_limit > self.x_limit:
            for idy in range(self.y_limit + 1):
                self.map[idy].extend([0] * (new_limit - self.x_limit))
            self.x_limit = new_limit

    def add_vent_flat(self, vent: VectorLine) -> None:
        self.update_y_limit(vent.origin.y)
        self.update_x_limit(vent.origin.x)

        self.update_y_limit(vent.final.y)
        self.update_x_limit(vent.final.x)

        if vent.is_flat:
            y_step = [1, -1][vent.final.y < vent.origin.y]
            x_step = [1, -1][vent.final.x < vent.origin.x]
            for idy in range(vent.origin.y, vent.final.y + y_step, y_step):
                for idx in range(vent.origin.x, vent.final.x + x_step, x_step):
                    self.map[idy][idx] += 1
                    if 3 > self.map[idy][idx] > 1:
                        self.crossing_count += 1

    def add_all_kinds(self, vent: VectorLine) -> None:
        self.update_y_limit(vent.origin.y)
        self.update_x_limit(vent.origin.x)

        self.update_y_limit(vent.final.y)
        self.update_x_limit(vent.final.x)

        keep_moving = True
        idy = vent.origin.y
        idx = vent.origin.x
        while keep_moving:
            self.map[idy][idx] += 1
            if 3 > self.map[idy][idx] > 1:
                self.crossing_count += 1
            if idy == vent.final.y and idx == vent.final.x:
                keep_moving = False
            if idy != vent.final.y:
                idy += [1, -1][vent.final.y < vent.origin.y]
            if idx != vent.final.x:
                idx += [1, -1][vent.final.x < vent.origin.x]


if __name__ == '__main__':
    with open("./data/day5.txt") as file:
        input_data = file.read().splitlines()
        vectors = create_vectors(input_data)
        vent_map = VentMap()
        vent_map_part_two = VentMap()
        for vector in vectors:
            vent_map.add_vent_flat(vector)
            vent_map_part_two.add_all_kinds(vector)
        print(vent_map.crossing_count)
        print(vent_map_part_two.crossing_count)
