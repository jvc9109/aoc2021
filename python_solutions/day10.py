from typing import List, Tuple


def solve_problems(data: List[str]) -> Tuple[int, int]:
    openers = {'[': ']', '(': ')', '<': '>', '{': '}'}
    points = {
        ']': 57, ')': 3, '>': 25137, '}': 1197
    }
    points_incomplete = {
        ']': 2, ')': 1, '>': 4, '}': 3
    }
    total = 0
    res = []
    scores = []
    for line in data:
        expected_terminator = []
        for char in line:
            if char in openers.keys():
                expected_terminator.append(openers[char])
            else:
                if char == expected_terminator[-1]:
                    expected_terminator.pop()
                else:
                    res.append(char)
                    break
        else:
            score = 0
            if len(expected_terminator) > 0:
                expected_terminator.reverse()
                for char in expected_terminator:
                    score *= 5
                    score += points_incomplete[char]
                scores.append(score)
    scores.sort()
    for term in res:
        total += points[term]

    return total, scores[len(scores) // 2]


with open("../data/day10.txt") as file:
    data = file.read().splitlines()
    print(solve_problems(data))
