from collections import UserList
from typing import List, Tuple, Optional, Iterable, Sequence, SupportsIndex


class Number:
    drawn: bool
    value: int

    def __init__(self, value: int):
        self.drawn = False
        self.value = value

    def draw(self) -> None:
        self.drawn = True

    def is_marked(self) -> bool:
        return self.drawn


class Numbers(UserList):
    data: List[Number]

    def __init__(self, number: List[Number]):
        super().__init__()
        self.extend(number)

    def is_full(self) -> bool:
        for number in self.data:
            if not number.drawn:
                return False
        return True

    def from_position(self, position) -> Number:
        return self.data[position]

    def draw_number(self, check: int) -> bool:
        for number in self.data:
            if number.value == check and not number.drawn:
                number.draw()
                return True
        else:
            return False


class CollectionNumbers(UserList):
    data: List[Numbers]

    def __init__(self, *numbers: Numbers):
        super().__init__()
        self.extend(numbers)


class Board:
    rows: CollectionNumbers
    total: int

    def __init__(self, rows: CollectionNumbers):
        super().__init__()
        self.rows = rows
        self.total = 0
        self.get_total()

    def get_total(self) -> None:
        for row in self.rows:
            for number in row:
                self.total += number.value

    def check_bingo(self) -> bool:
        for row in self.rows:
            if row.is_full():
                return True

        for index_col in range(len(self.rows[0])):
            for row in self.rows:
                if not row[index_col].drawn:
                    break
            else:
                return True
        return False

    def draw_number(self, draw: int) -> None:
        for row in self.rows:
            if row.draw_number(draw):
                self.total -= draw
                break

    def get_magic_number(self, last_draw: int) -> int:
        return self.total * last_draw


def build_boards(data: list) -> List[Board]:
    result = []
    rows = CollectionNumbers()
    for line in data[2:]:
        if line == '':
            board = Board(rows)
            result.append(board)
            rows = []
            continue
        else:
            rows.append(Numbers([Number(int(i)) for i in line.split()]))
    else:
        board = Board(rows)
        result.append(board)

    return result


def play_bingo(draw_numbers: List[int], boards_playing: List[Board]) -> Optional[Tuple[Board, int]]:
    for idx, draw in enumerate(draw_numbers):
        for board in boards_playing:
            board.draw_number(draw)
            if idx > 5 and board.check_bingo():
                return board, draw

    return None


def get_last_winner(draw_numbers: List[int], boards_playing: List[Board]) -> Optional[Tuple[Board, int]]:
    last_board: Optional[Board] = None
    when: Optional[int] = None
    for idx, draw in enumerate(draw_numbers):
        for board_idx, board in enumerate(boards_playing):
            if board is not None:
                board.draw_number(draw)
                if board.check_bingo():
                    last_board = board
                    last_board.draw_number(draw)
                    when = draw
                    boards_playing[board_idx] = None

    return last_board, when


if __name__ == '__main__':
    with open("./data/day4.txt") as file:
        data = file.read().splitlines()
        draws = [int(i) for i in data[0].split(',')]
        boards = build_boards(data)

        winner, last_number = play_bingo(draws, boards)
        print(winner.get_magic_number(last_number))

        boards = build_boards(data)
        winner, a_number = get_last_winner(draws, boards)
        print(winner.get_magic_number(a_number))
