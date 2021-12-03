def obtain_most_common_bit(lines: list, position: int) -> str:
    bits = {'1': 0, '0': 0}
    for line in lines:
        bits[line[position]] += 1
    return max(bits, key=bits.get)


def obtain_less_common_bit(lines: list, position: int) -> str:
    bits = {'0': 0, '1': 0}
    for line in lines:
        bits[line[position]] += 1
    return min(bits, key=bits.get)


def obtain_gamma_value(lines: list) -> str:
    gamma = ''
    for position in range(len(lines[0])):
        gamma += obtain_most_common_bit(lines, position)

    return gamma


def obtain_epsilon_from_gamma(gamma: str) -> str:
    epsilon = ''
    for bit in gamma:
        epsilon += '1' if bit == '0' else '0'

    return epsilon


def filter_number_bit_criteria(position, bit_value, lines):
    numbers = []
    for line in lines:
        if line[position] == bit_value:
            numbers.append(line)

    return numbers


def obtain_oxygen_rating(lines: list, carry: int) -> int:
    carry_bit = '1'
    if obtain_most_common_bit(lines, carry) == '0':
        carry_bit = '0'
    total = filter_number_bit_criteria(carry, carry_bit, lines)
    if len(total) > 1:
        return obtain_oxygen_rating(total, carry + 1)

    return int(total[0], 2)


def obtain_co2_rating(lines: list, carry: int) -> int:
    carry_bit = '0'
    if obtain_less_common_bit(lines, carry) == '1':
        carry_bit = '1'

    total = filter_number_bit_criteria(carry, carry_bit, lines)

    if len(total) > 1:
        return obtain_co2_rating(total, carry + 1)

    return int(total[0], 2)


if __name__ == '__main__':
    with open("./data/day3.txt") as file:
        data = file.read().splitlines()
        gamma = obtain_gamma_value(data)
        epsilon = obtain_epsilon_from_gamma(gamma)
        print(int(gamma,2)*int(epsilon,2 ))
        oxygen = obtain_oxygen_rating(data, 0)
        co2 = obtain_co2_rating(data, 0)
        print(oxygen * co2)
