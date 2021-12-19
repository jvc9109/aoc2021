from typing import Tuple, Iterable, List


class Octopus:
    position: Tuple[int, int]
    should_flash: bool
    energy: int
    should_propagate: bool

    def __init__(self, position: Tuple[int, int], energy_level: int) -> None:
        super().__init__()
        self.should_flash = energy_level > 9
        self.should_propagate = False
        self.energy = energy_level
        self.position = position

    def add_energy(self):
        self.energy += 1
        self.should_flash = self.energy > 9
        if self.energy == 10:
            self.should_propagate = True

    def prepare_next_step(self) -> int:
        self.should_flash = False
        self.energy = 0 if self.energy > 9 else self.energy

        return 1 if self.energy == 0 else 0

    def get_adjacent(self, max_y, max_x) -> Iterable[Tuple[int, int]]:
        adjacent = []
        for idy in range(-1, 2):
            for idx in range(-1, 2):
                next_adjacent = (self.position[0] + idy, self.position[1] + idx)
                if 0 <= next_adjacent[0] < max_y and 0 <= next_adjacent[1] < max_x:
                    yield next_adjacent
        self.should_propagate = len(adjacent) > 0
        return adjacent


def propagate(octo_map: List[List[Octopus]], y_limit: int, x_limit: int):
    keep_propagating = True
    while keep_propagating:
        lighted = []
        for line in octo_map:
            for octo in line:
                if octo.should_propagate:
                    for idy, idx in octo.get_adjacent(y_limit, x_limit):
                        octo_map[idy][idx].add_energy()
                        if octo_map[idy][idx].should_flash:
                            lighted.append(0)
        keep_propagating = len(lighted) > 0


def print_status(octo_map: List[List[Octopus]]):
    res = []
    for line in octo_map:
        pos = ''
        for octo in line:
            pos += str(octo.energy)
        res.append(pos)

    print('\n'.join(res))
    print()
    print()


def reset_counters(octo_map: List[List[Octopus]]) -> int:
    res = 0
    for line in octo_map:
        for octo in line:
            res += octo.prepare_next_step()
    return res


if __name__ == '__main__':
    with open("../data/day11.txt") as file:
        data = file.read().splitlines()
        map = []
        for idy, row in enumerate(data):
            map.append([Octopus((idy, idx), int(energy)) for idx, energy in enumerate(row)])
        max_x = len(map[0])
        max_y = len(map)
        lighted = 0
        for step in range(1, 300):
            print(f'Init Step {step}')
            for row in map:
                for octopus in row:
                    octopus.add_energy()
            propagate(map, max_y, max_x)
            flashed = reset_counters(map)
            if flashed == 100:
                print(step)
                break
            lighted += reset_counters(map)
    print(lighted)
