from typing import List, Dict


class Edge:
    point1: str
    point2: str

    def __init__(self, point1: str, point2: str) -> None:
        self.point1 = point1
        self.point2 = point2


class CaveSize:
    BIG = 'big'
    SMALL = 'small'


class CaveSys:
    edges: Dict[str, List[str]]

    def __init__(self, caves: List[Edge]) -> None:
        self.edges = {}
        for cave in caves:
            if cave.point1 not in self.edges.keys():
                self.edges[cave.point1] = []
            if cave.point2 not in self.edges.keys():
                self.edges[cave.point2] = []

            self.edges[cave.point1].append(cave.point2)
            self.edges[cave.point2].append(cave.point1)

    @staticmethod
    def get_cave_size(name: str) -> str:
        return CaveSize.BIG if name.isupper() else CaveSize.SMALL

    def search_paths(self, start: str, end: str, partial_path: List[str]) -> List[List[str]]:

        new_partial = [k for k in partial_path]
        new_partial.append(start)

        if start == end:
            return [new_partial]

        candidates = [cave for cave in self.edges[start] if
                      self.get_cave_size(cave) == CaveSize.BIG or cave not in new_partial]
        paths = []
        for candidate in candidates:
            paths.extend(self.search_paths(candidate, end, new_partial))

        return paths

    def search_paths_v2(self, start: str, end: str, partial_path: List[str], can_repeat_small: bool = True) \
            -> List[List[str]]:
        new_partial = [k for k in partial_path]
        new_partial.append(start)

        if start == end:
            return [new_partial]

        candidates = []

        for cave in self.edges[start]:
            if self.get_cave_size(cave) == CaveSize.BIG:
                candidates.append((cave, can_repeat_small))
            elif cave == 'start' and cave in new_partial:
                continue
            elif (cave == 'start' or cave == 'end') and cave not in new_partial:
                candidates.append((cave, can_repeat_small))
            elif self.get_cave_size(cave) == CaveSize.SMALL and can_repeat_small and new_partial.count(cave) < 2:
                candidates.append((cave, can_repeat_small and new_partial.count(cave) < 1))
            elif self.get_cave_size(cave) == CaveSize.SMALL and cave not in new_partial:
                candidates.append((cave, can_repeat_small and new_partial.count(cave) < 1))
        paths = []
        for candidate, can_repeat in candidates:
            paths.extend(self.search_paths_v2(candidate, end, new_partial, can_repeat))

        return paths


def read_input(raw_nodes: str) -> List[Edge]:
    res = []
    for node in raw_nodes.splitlines():
        [start, end] = node.split('-')
        res.append(Edge(start, end))
    return res


if __name__ == '__main__':
    input_test = 'start-A\nstart-b\nA-c\nA-b\nb-d\nA-end\nb-end'
    graph_test = CaveSys(read_input(input_test))
    assert (len(graph_test.search_paths('start', 'end', [])) == 10)
    assert (len(graph_test.search_paths_v2('start', 'end', [], True)) == 36)

    with open("../data/day12.txt") as file:
        data = file.read()
        graph = CaveSys(read_input(data))
        print(len(graph.search_paths('start', 'end', [])))

        print(len(graph.search_paths_v2('start', 'end', [], True)))
