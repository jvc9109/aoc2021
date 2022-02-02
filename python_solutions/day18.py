from __future__ import annotations

import math
import re
from typing import Optional


class Pair:
    left: Optional[Pair, int]
    right: Optional[Pair, int]
    level: int
    parent: Optional[Pair]

    def __init__(self, left, right, level) -> None:
        self.left = left
        self.right = right
        self.level = level
        self.parent = None

    def setParent(self, parent: Pair) -> None:
        self.parent = parent

    def mutate_left(self, left) -> None:
        self.left = left

    def mutate_right(self, right) -> None:
        self.right = right

    def mutate_level(self, level) -> None:
        self.level = level

    def get_left_first_number(self) -> Optional[int]:
        if self.parent is not None:
            if isinstance(self.parent.left, Pair):
                return self.parent.get_left_first_number()
            else:
                return self.parent.left
        else:
            return None

    def get_right_first_number(self) -> Optional[int]:
        if self.parent is not None:
            if isinstance(self.parent.right, Pair):
                return self.parent.get_right_first_number()
            else:
                return self.parent.right
        else:
            return None

    def __eq__(self, other: Pair) -> bool:
        if not isinstance(other, Pair):
            return False
        if isinstance(self.left, Pair) and isinstance(other.left, Pair) or (
                not isinstance(self.left, Pair) and not isinstance(other.left, Pair)):
            are_left_eq = self.left == other.left
        else:
            return False

        if isinstance(self.right, Pair) and isinstance(other.right, Pair) or (
                not isinstance(self.right, Pair) and not isinstance(other.right, Pair)):
            are_right_eq = self.right == other.right
        else:
            return False

        return are_right_eq and are_left_eq


def get_linked_pairs(data: str, from_level=0) -> Pair:
    nest = from_level
    left = None
    right = None
    switch_right = False
    parent = None
    switch_append = True
    childs = []
    pair = None

    for idx, char in enumerate(data):
        if len(childs) == 2:
            left = Pair(childs[0], childs[1], childs[0].level - 1, )
            childs[0].setParent(left)
            childs[1].setParent(left)
            childs = []
        if char == '[' and idx > 0 and data[idx - 1] == '[':
            nest += 1
        elif char == '[' and idx > 0 and data[idx - 1] != '[':
            right = get_linked_pairs(data[idx:], nest + 1)
            pair = Pair(left, right, nest)
            if isinstance(left, Pair):
                left.setParent(pair)
            if isinstance(right, Pair):
                right.setParent(pair)
            return pair
        if char == ']':
            if left is not None and right is not None:
                pair = Pair(left, right, nest)
                if switch_append:
                    childs.append(pair)
                    switch_append = False
                if isinstance(left, Pair):
                    left.setParent(pair)
                if isinstance(right, Pair):
                    right.setParent(pair)
                left = pair
                right = None
                switch_right = True
            nest -= 1
        elif char.isnumeric() and not switch_right:
            left = int(char)
        elif char.isnumeric() and switch_right:
            right = int(char)
            switch_right = False
        elif char == ',':
            switch_right = True

    return pair


def explode(number: str) -> str:
    offset = 0
    digits_pattern = re.compile(r"\[\d+,\d+\]")
    single_digit_patter = re.compile(r'\d+')
    for p in re.findall(digits_pattern, number):
        pair = re.search(re.escape(p), number[offset:])
        left_brackets = number[: pair.start() + offset].count("[")
        right_brackets = number[: pair.start() + offset].count("]")
        if left_brackets - right_brackets >= 4:
            x, y = pair.group()[1:-1].split(",")
            # split the string into two parts at the pair
            # flip left side around so we get the first num going backwards
            left = number[: pair.start() + offset][::-1]

            right = number[pair.end() + offset:]
            # look left
            search_left = re.search(single_digit_patter, left)
            if search_left:
                # need to find the rightmost match not the first
                amt = int(left[search_left.start(): search_left.end()][::-1]) + int(x)
                left = f"{left[:search_left.start()]}{str(amt)[::-1]}{left[search_left.end():]}"
            # look right
            search_right = re.search(single_digit_patter, right)
            if search_right:
                amt = int(right[search_right.start(): search_right.end()]) + int(y)
                right = (
                    f"{right[:search_right.start()]}{amt}{right[search_right.end():]}"
                )
            number = f"{left[::-1]}0{right}"
            break
        else:
            offset = pair.end() + offset
    return number


def split(number: str) -> str:
    dd = re.search("\d\d", number)
    if dd:
        left = number[: dd.start()]
        right = number[dd.end():]
        left_digit = int(math.floor(int(dd.group()) / 2))
        right_digit = int(math.ceil(int(dd.group()) / 2))
        number = f"{left}[{left_digit},{right_digit}]{right}"
    return number


def test_case_explode() -> None:
    input_test = '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'
    expected = '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
    exploted = explode(input_test)
    assert expected == exploted


def test_case_split() -> None:
    input_test = '[[[[0,7],4],[15,[0,13]]],[1,1]]'
    expected = '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'
    splitted = split(input_test)
    assert splitted == expected


if __name__ == '__main__':
    test_case_explode()
    test_case_split()
