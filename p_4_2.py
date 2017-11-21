# Retrieve i-th bit
# Retrieve j-th bit
# If they differ
#     flip i-th bit
#     flip j-th bit

# Using actual swapping of bits
def swap_bits1(number, i, j):
    i_th = (number >> i) & 0x1
    j_th = (number >> j) & 0x1

    if i_th != j_th:
        number = (i_th << j) | (~(0x1 << j) & number)
        number = (j_th << i) | (~(0x1 << i) & number)

    return number

# Using bit flippin
def swap_bits2(number, i, j):
    i_th = (number >> i) & 0x1
    j_th = (number >> j) & 0x1

    if i_th != j_th and i != j:
        number ^= 0x1 << i
        number ^= 0x1 << j

    return number

x = 0b10010101
i = 2
j = 6
print(bin(swap_bits1(x, i, j)))
print(bin(swap_bits2(x, i, j)))
