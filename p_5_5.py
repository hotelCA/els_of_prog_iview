def eliminate_dups(A):
    if 0 <= len(A) <= 1:
        return len(A)
    i, j = 0, 1
    while j < len(A):
        if A[j] > A[i]:
            i += 1
            A[i] = A[j]
        j += 1
    return i+1

A = [1,1,2,3,3,3,5,5,6,7,8,99]
print(eliminate_dups(A))
print(A)