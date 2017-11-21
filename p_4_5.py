import random

def multiply(x, y):

    def mult(x, y):
        y >>= 1
        while y != 0:
            x <<= 1
            y >>= 1
        return x

    def add(x, y):
        carry = 0
        reverse_sum = []
        result = 0
        while x != 0 or y != 0 or carry != 0:
            reverse_sum.append(carry ^ (x & 1) ^ (y & 1))
            carry = (carry & (x & 1)) or (carry & (y & 1)) or ((y & 1) & (x & 1))
            x, y = x >> 1, y >> 1
        while reverse_sum != []:
            result |= reverse_sum[-1]
            result <<= 1
            del(reverse_sum[-1])
        return result >> 1


    running_sum = 0
    multiplier = 1
    while y != 0:
        if y & 1 == 1:
            running_sum = add(running_sum, mult(x, multiplier))
        multiplier <<= 1
        y >>= 1
    return running_sum

print(multiply(11,11))
A = [1,2,3,4]
random.shuffle(A)
print(random.choice(A))