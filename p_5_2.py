# set carry to false
# iterate through array backwards
#
#         if digit is less than 9
#             increment by 1
#             break
#         else
#             set digit to 0
#             set carry to true
#
# if carry is true
#     prepend 1

def incrementer(array_of_digits):
    carry = False
    for i, digit in reversed(list(enumerate(array_of_digits))):
        if digit < 9:
            array_of_digits[i] += 1
            carry = False
            break
        else:
            array_of_digits[i] = 0
            carry = True
    if carry:
        array_of_digits.insert(0, 1)
    return array_of_digits

def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 0
        A.insert(0,1)
    return A

# PSEUDOCODE
# set carry to 0
# iterate through both strings from least significant digit
#     add the two digits + carry
#     if sum is bigger than 9
#         change sum to sum mod 10
#         set carry to 1
#     else
#         set carry to 0

def adder(numbA, numbB):
    carry = 0
    sum = []
    remainder_number = [0]
    len_difference = len(numbA) - len(numbB)

    if len_difference > 0:
        remainder_number = numbA[0:len_difference]
    elif len_difference < 0:
        remainder_number = numbB[0:abs(len_difference)]

    remainder_number = [int(x) for x in remainder_number]

    for x, y in zip(reversed(numbA), reversed(numbB)):
        sum.insert(0, carry + int(x) + int(y))
        if sum[0] > 9:
            sum[0] %= 10
            carry = 1
        else:
            carry = 0

    if carry == 0:
        if remainder_number[0] != 0:
            sum = remainder_number + sum
    else:
        sum = incrementer(remainder_number) + sum

    return sum


# print(incrementer([8,9,9]))
# print(incrementer([1,2,9]))
# print(incrementer([9,9]))
# print(incrementer([1,0,9]))
# print(incrementer([1,0,0]))
print(adder('431234567', '837261234'))
print(431234567 + 837261234)


