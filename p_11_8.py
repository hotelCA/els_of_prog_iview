import math
import random

def find_kth_largest(A, k):
    if k > len(A) or k <= 0:
        return None
    start_index, end_index = 0, len(A) - 1
    while True:
        bigger = 0
        pivot = A[end_index]
        current = start_index
        # print('pivot: {}'.format(pivot))
        # Pivot elements around the chosen pivot
        while current <= (end_index-bigger-1):
            if A[current] <= pivot:
                current += 1
            else:
                A[current], A[end_index-bigger-1] = A[end_index-bigger-1], A[current]
                bigger += 1
        # Put pivot element in it's correct place
        A[end_index], A[end_index-bigger] = A[end_index-bigger], A[end_index]
        # print('bigger: {}, k: {}, s: {}, e: {}'.format(bigger, k, start_index, end_index))
        # Adjust the range of the next pivot
        if bigger > k-1:
            start_index = end_index - bigger + 1
        elif bigger < k-1:
            end_index = end_index - bigger - 1
            k = k - bigger - 1
        else:
            print(A)
            return pivot
            
# Sorted: 2,3,4,5,7,8,9,11,17 
A = [2,11,17,4,9,7,8,5,3]
# print(find_kth_largest(A, 3))