import sys
import math

def find_min_max(A):
    smallest, largest = sys.maxsize, 0
    for i in range(0, math.ceil(len(A)/2)):
        a, b = A[i], A[-(i+1)]
        if a < b:
            smallest = min(smallest, a)
            largest = max(largest, b)
        else:
            smallest = min(smallest, b)
            largest = max(largest, a)
    print('Smallest = {}\nLargest = {}'.format(smallest, largest))
    
A = [3,6,4,7,8,5,0,1,-9,100,32,55,-1,-6,4,65]
find_min_max(A)