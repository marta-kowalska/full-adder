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


'''
XOR
a b o
0 0 0
0 1 1
1 0 1
1 1 0
'''




def get_number(number_bits):
    number_str = ''
    for bit in number_bits:
        number_str += str(bit)
    return int(number_str, 2)


def add(a, b):
    result = []
    carry = 0
    bit_a = get_bit(a, 0)
    bit_b = get_bit(b, 0)
    while(carry or bit_a or bit_b):
        sum_bits = get_sum(bit_a, bit_b, carry)
        carry = get_carry(bit_a, bit_b, carry)
        result.insert(0, sum_bits)
        a = a >> 1
        b = b >> 1
        bit_a = get_bit(a, 0)
        bit_b = get_bit(b, 0)
    return get_number(result)




print(add(7, 11))
