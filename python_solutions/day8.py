from typing import List, Tuple


def get_six_len_sig(inputs: List[str], four_char: str, one_char: str) -> Tuple[str, str, str]:
    candidates = []
    nine_char = ''
    for char in inputs:
        if len(char) == 6:
            candidates.append(char)

    for idx, candidate in enumerate(candidates):
        for char in four_char:
            if char not in candidate:
                break
        else:
            nine_char = candidate
            candidates.pop(idx)
            break

    for idx, candidate in enumerate(candidates):
        for char in one_char:
            if char not in candidate:
                six_char = candidate
                candidates.pop(idx)
                zero_char = candidates[0]
                return nine_char, six_char, zero_char
        else:
            zero_char = candidate
            candidates.pop(idx)
            six_char = candidates[0]
            return nine_char, six_char, zero_char


def get_five_len_sig(inputs: List[str], one_char: str, four_char: str) -> Tuple[str, str, str]:
    candidates = []
    three_char = ''
    two_char = ''
    five_char = ''
    for char in inputs:
        if len(char) == 5:
            candidates.append(char)

    for idx, candidate in enumerate(candidates):
        for char in one_char:
            if char not in candidate:
                break
        else:
            three_char = candidate
            candidates.pop(idx)
            break

    for idx, candidate in enumerate(candidates):
        acc = 0
        for char in four_char:
            if char not in candidate:
                acc += 1
        if acc == 2:
            two_char = candidate
            candidates.pop(idx)
            five_char = candidates[0]
            break
        else:
            five_char = candidate
            candidates.pop(idx)
            two_char = candidates[0]
            break

    return two_char, three_char, five_char


def get_easy_sig(inputs):
    for sig in inputs:
        if len(sig) == 2:
            one_char = sig
        elif len(sig) == 4:
            four_char = sig
        elif len(sig) == 3:
            seven_char = sig
        elif len(sig) == 7:
            eigth_char = sig
    return one_char, four_char, seven_char, eigth_char


def sort_string(str_input):
    return ''.join(sorted(str_input))


def part_two(lines):
    total = 0
    for line in data:
        input, output = line.split('|')
        input = input.strip()

        one, four, seven, eight = get_easy_sig(input.split())
        nine, six, zero = get_six_len_sig(input.split(), four, one)
        two, three, five = get_five_len_sig(input.split(), one, four)
        numbers = {
            sort_string(zero): "0",
            sort_string(one): "1",
            sort_string(two): "2",
            sort_string(three): "3",
            sort_string(four): "4",
            sort_string(five): "5",
            sort_string(six): "6",
            sort_string(seven): "7",
            sort_string(eight): "8",
            sort_string(nine): "9"
        }
        res = ''
        try:
            for dig in output.split():
                dig = sort_string(dig)
                res += numbers[dig]
        except:
            print('hola')
        total += int(res)
    print(total)


def part_one(lines):
    times = 0
    for line in data:
        input, output = line.split('|')
        output = output.strip()
        for digit in output.split():
            if len(digit) in [2, 3, 4, 7]:
                times += 1
    print(times)


if __name__ == '__main__':
    with open("../data/day8.txt") as file:
        data = file.read().splitlines()
        part_one(data)
        part_two(data)
