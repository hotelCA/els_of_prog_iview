# Brute force would be to iterate over every bit and inserting it in a new number
def reverse_bits1(x):
    result = 0
    for i in range(0, 64):
        result |= ((x >> i) & 0x1) << (63 - i)

    return result

# Improvement would be to iterate through 32 least significant bits and swap them with the most significant
# def reverse_bits2(x):
#     result = 0
#     for i in range(0, 32):
        #swap bit i and bit 63 - i

# Another improvement is to use a look up table of size 2^16. Then swap quadrants.
# PSEUDOCODE:
#   swap first and last quadrant
#   swap second and third quadrant
#   use look-up for each quadrant

print(bin(reverse_bits1(0b1100101)))