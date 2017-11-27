import sys
from functools import reduce

def max_n_minus_one_product(A):
    if not A:
        return None

    min_pos, max_neg, min_neg = 0, 0, 0
    negative = 0
    non_negative_count = 0
    negative_count = 0
    skip_index = None
    for i in range(0, len(A)):
        if A[i] < 0:
            negative_count += 1
            negative ^= 1
            if A[i] > A[min_neg] or A[min_neg] > 0:
                min_neg = i
            if A[i] < A[max_neg]:
                max_neg = i
        else:
            non_negative_count += 1
            if A[i] < A[min_pos]:
                min_pos = i
    
    if negative_count == 0:
        skip_index = min_pos
    elif negative:
        skip_index = min_neg
    elif positive_count == 0:
        skip_index = max_neg
    else:
        skip_index = min_pos

    product = 1
    print('skip index: {}'.format(skip_index))
    for i in range(len(A)):
        if i != skip_index:
            product *= A[i]

    return product

def max_n_minus_one_product_test(A):
    max_prod = -sys.maxsize
    for i in range(len(A)):
        product = 1
        for j in range(len(A)):
            if j != i:
                product *= A[j]
        if product > max_prod:
            max_prod = product
    return max_prod

A = [2,3,4,5,-6,43,4,50,4,2,6,87,4,-5,-4,76,9,3,1,78,5,3,2]
print(max_n_minus_one_product(A))
print(max_n_minus_one_product_test(A))
