from typing import Tuple


class OperatorType:
    LITERAL = 4
    SUM = 0
    PRODUCT = 1
    MIN = 2
    MAX = 3
    GT = 5
    LT = 6
    EQ = 7


class Packet:
    def __init__(self, version, id, value=None) -> None:
        self.version = version
        self.id = id
        self.value = value

    def obtain_total_versions(self) -> int:
        res = self.version
        for value in self.value:
            if isinstance(value, Packet):
                res += value.obtain_total_versions()
        return res

    def compute_value(self) -> int:
        if self.id == OperatorType.SUM:
            return self.sum_all_packets()
        elif self.id == OperatorType.LITERAL:
            return self.obtain_number()
        elif self.id == OperatorType.PRODUCT:
            return self.prod_of_packets()
        elif self.id == OperatorType.MIN:
            return self.obtain_min()
        elif self.id == OperatorType.MAX:
            return self.obtain_max()
        elif self.id == OperatorType.GT:
            return self.obtain_gt()
        elif self.id == OperatorType.LT:
            return self.obtain_lt()
        elif self.id == OperatorType.EQ:
            return self.obtain_eq()

        raise Exception

    def obtain_number(self) -> int:
        return int(''.join(self.value), 2)

    def sum_all_packets(self) -> int:
        total = 0
        for packet in self.value:
            if not isinstance(packet, Packet):
                raise Exception
            total += packet.compute_value()

        return total

    def prod_of_packets(self) -> int:
        total = 1
        for packet in self.value:
            if not isinstance(packet, Packet):
                raise Exception
            total *= packet.compute_value()

        return total

    def obtain_min(self) -> int:
        cum_vals = []
        for packet in self.value:
            if not isinstance(packet, Packet):
                raise Exception
            cum_vals.append(packet.compute_value())
        return min(cum_vals)

    def obtain_max(self) -> int:
        cum_vals = []
        for packet in self.value:
            if not isinstance(packet, Packet):
                raise Exception
            cum_vals.append(packet.compute_value())
        return max(cum_vals)

    def obtain_gt(self) -> int:
        cum_vals = []
        for packet in self.value:
            if not isinstance(packet, Packet):
                raise Exception
            cum_vals.append(packet.compute_value())
        return int(cum_vals[0] > cum_vals[1])

    def obtain_lt(self) -> int:
        cum_vals = []
        for packet in self.value:
            if not isinstance(packet, Packet):
                raise Exception
            cum_vals.append(packet.compute_value())
        return int(cum_vals[0] < cum_vals[1])

    def obtain_eq(self) -> int:
        cum_vals = []
        for packet in self.value:
            if not isinstance(packet, Packet):
                raise Exception
            cum_vals.append(packet.compute_value())
        return int(cum_vals[0] == cum_vals[1])


def hex_to_bit(hex_num: str) -> str:
    translate = {'0': '0000',
                 '1': '0001',
                 '2': '0010',
                 '3': '0011',
                 '4': '0100',
                 '5': '0101',
                 '6': '0110',
                 '7': '0111',
                 '8': '1000',
                 '9': '1001',
                 'A': '1010',
                 'B': '1011',
                 'C': '1100',
                 'D': '1101',
                 'E': '1110',
                 'F': '1111'}

    return ''.join([translate.get(i) for i in hex_num])


def get_packet_and_rest(bits: str) -> Tuple[Packet, str]:
    values = []
    packets = []
    bits_to_explot = ''
    version = int(bits[0:3], 2)
    id = int(bits[3:6], 2)
    if id == OperatorType.LITERAL:
        carry = 7
        keep_moving = 1
        while keep_moving != 0:
            keep_moving = int(bits[carry - 1])
            values.append(bits[carry:carry + 4])
            carry += 5
        remaining = bits[carry - 1:]
        return Packet(version, id, values), remaining

    elif int(bits[6]) == 1:
        number_sub_packets = int(bits[7:18], 2)
        bits_to_explot = bits[18:]
        for i in range(number_sub_packets):
            res_packs, bits_to_explot = get_packet_and_rest(bits_to_explot)
            packets.append(res_packs)

    elif int(bits[6]) == 0:
        bits_to_explot = bits[22:]
        len_to_explot = int(bits[7:22], 2)
        len_remain = len(bits_to_explot)
        exploited = 0
        while len_to_explot - exploited != 0:
            res_packs, bits_to_explot = get_packet_and_rest(bits_to_explot)
            packets.append(res_packs)
            exploited = len_remain - len(bits_to_explot)

    return Packet(version, id, packets), bits_to_explot


if __name__ == '__main__':
    input_test = '8A004A801A8002F478'
    packs, _ = get_packet_and_rest(hex_to_bit(input_test))
    assert (packs.obtain_total_versions() == 16)

    input_test = '620080001611562C8802118E34'
    packs, _ = get_packet_and_rest(hex_to_bit(input_test))
    assert (packs.obtain_total_versions() == 12)

    input_test = 'C0015000016115A2E0802F182340'
    packs, _ = get_packet_and_rest(hex_to_bit(input_test))
    assert (packs.obtain_total_versions() == 23)

    input_test = 'A0016C880162017C3686B18A3D4780'
    packs, _ = get_packet_and_rest(hex_to_bit(input_test))
    assert (packs.obtain_total_versions() == 31)

    input_test = 'C200B40A82'
    packs, _ = get_packet_and_rest(hex_to_bit(input_test))
    assert (packs.compute_value() == 3)

    input_test = '04005AC33890'
    packs, _ = get_packet_and_rest(hex_to_bit(input_test))
    assert (packs.compute_value() == 54)

    input_test = '880086C3E88112'
    packs, _ = get_packet_and_rest(hex_to_bit(input_test))
    assert (packs.compute_value() == 7)

    input_test = 'CE00C43D881120'
    packs, _ = get_packet_and_rest(hex_to_bit(input_test))
    assert (packs.compute_value() == 9)

    input_test = 'D8005AC2A8F0'
    packs, _ = get_packet_and_rest(hex_to_bit(input_test))
    assert (packs.compute_value() == 1)

    input_test = 'F600BC2D8F'
    packs, _ = get_packet_and_rest(hex_to_bit(input_test))
    assert (packs.compute_value() == 0)

    input_test = '9C005AC2F8F0'
    packs, _ = get_packet_and_rest(hex_to_bit(input_test))
    assert (packs.compute_value() == 0)

    input_test = '9C0141080250320F1802104A08'
    packs, _ = get_packet_and_rest(hex_to_bit(input_test))
    assert (packs.compute_value() == 1)

    with open("../data/day16.txt") as file:
        data = file.read()
        packs, _ = get_packet_and_rest(hex_to_bit(data))
        print(packs.obtain_total_versions())
        print(packs.compute_value())
