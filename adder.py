def get_sum(bit_a, bit_b, carry):
    return (bit_a ^ bit_b ^ carry)


def get_carry(bit_a, bit_b, carry):
    return (bit_a and bit_b) or \
           (not bit_a and bit_b and carry) or \
           (bit_a and not bit_b and carry)


def get_bit(number, bit_position):
    number = number >> bit_position
    number = number & 1
    return number


def set_bit(number, bit_position):
    mask = 1 << bit_position
    number = number | mask
    return number


def get_number(number_bits):
    number_str = ''.join(str(digit) for digit in number_bits)
    return int(number_str, 2)


def add(a, b):
    result = []
    carry = 0
    while(carry or a or b):
        bit_a = get_bit(a, 0)
        bit_b = get_bit(b, 0)
        sum_bit = get_sum(bit_a, bit_b, carry)
        carry = get_carry(bit_a, bit_b, carry)
        a = a >> 1
        b = b >> 1
        result.insert(0, sum_bit)
    return get_number(result)



if __name__ == '__main__':
    print(add(3, 5))
