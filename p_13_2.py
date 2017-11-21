def merge_sorted_arrays(A, m, B, n):
    smallest = m + n -1
    i, j = m - 1, n - 1
    while i >= 0 or j >= 0:
        if j < 0:
            A[smallest] = A[i]
            i -= 1
        elif i < 0:
            A[smallest] = B[j]
            j -= 1
        elif A[i] >= B[j]:
            A[smallest] = A[i]
            i -= 1
        else:
            A[smallest] = B[j]
            j -= 1
        smallest -= 1
    return A

A = [1,3,5,6] + 10 * [None]
B = [2,2,4,7,8,9]
m = len(list(filter(lambda x: x is not None, A)))
n = len(B)
print(merge_sorted_arrays(A,m,B,n))