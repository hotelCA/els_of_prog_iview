import string

def concat():
    return ''.join([str(num) for num in range(10)])

def string_to_int(string_num):
    result, sign = 0, 1
    if string_num[0] == '-':
        string_num = string_num[1:]
        sign = -1
    for digit in string_num:
        result = (10 * result) + string.digits.index(digit)
    return sign * result

def int_to_string(num):
    s = []
    negative = False
    if num < 0:
        negative, num = True, -num

    while True:
        s.append(chr(ord('0') + num % 10))
        num //= 10
        if num == 0:
            break

    return ('-' if negative else '') + ''.join(reversed(s))


print(string_to_int('123'))
print(string_to_int('-123'))
print(string_to_int('0'))
print(string_to_int('1'))
print(string_to_int('-1'))

print(int_to_string(123))
print(int_to_string(-123))
print(int_to_string(0))
print(int_to_string(1))
print(int_to_string(-1))


