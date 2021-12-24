from typing import List, Tuple, Dict
from collections import Counter


def solve(inp: List[str], steps: int):
    poly = inp[0]
    tmp_poly = Counter(a + b for a, b in zip(poly, poly[1:]))
    chars = Counter(poly)
    instructions = {}


    for inst in inp[2:]:
        pair, new = inst.split(' -> ')
        instructions[pair] = new

    for i in range(steps):
        tmp = Counter()
        for (c1, c2), value in tmp_poly.items():
            mc = instructions[c1 + c2]
            tmp[c1 + mc] += value
            tmp[mc + c2] += value
            chars[mc] += value
        tmp_poly = tmp
    return max(chars.values()) - min(chars.values())


if __name__ == '__main__':
    input_test = 'NNCB\n\nCH -> B\nHH -> N\nCB -> H\nNH -> C\nHB -> C\nHC -> B\nHN -> C\nNN -> C\nBH -> H\nNC -> ' \
                 'B\nNB -> B\nBN -> B\nBB -> N\nBC -> B\nCC -> N\nCN -> C\n'
    data = input_test.splitlines()

    assert (solve(data, 10) == 1588)
    assert (solve(data, 40) == 2188189693529)


    with open("../data/day14.txt") as file:
        data = file.read().splitlines()
        print(solve(data, 10))
        print(solve(data, 40))

