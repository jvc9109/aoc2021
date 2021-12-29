from heapq import heappop, heappush


def solve(data, i):
    m = [list(map(int, line)) for line in data.splitlines()]
    height, width = len(m), len(m[0])

    # Fast Dijkstra version
    heap, seen = [(0, 0, 0)], {(0, 0)}

    while heap:
        risk, r, c = heappop(heap)
        if r == i * height - 1 and c == i * width - 1:
            return risk

        for r_, c_ in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
            if 0 <= r_ < i * height and 0 <= c_ < i * width and (r_, c_) not in seen:
                rd, rm = divmod(r_, height)
                cd, cm = divmod(c_, width)

                seen.add((r_, c_))
                heappush(heap, (risk + (m[rm][cm] + rd + cd - 1) % 9 + 1, r_, c_))


if __name__ == '__main__':
    input_test = '1163751742\n1381373672\n2136511328\n3694931569\n7463417111\n1319128137\n1359912421\n3125421639' \
                 '\n1293138521\n2311944581'
    assert (solve(input_test, 1) == 40)
    assert (solve(input_test, 5) == 315)

    with open("../data/day15.txt") as file:
        data = file.read()
        print(solve(data, 1))
        print(solve(data, 5))
