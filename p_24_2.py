def find_first_missing_positive(A):
    temp, n = None, len(A)
    for i in range(n):
        if temp and temp != A[temp - 1]:
            temp_2 = A[temp - 1]
            A[temp-1] = temp
            if 1 <= temp_2 <= n:
                temp = temp_2
            i -= 1
        elif (1 <= A[i] <= n) and A[i] != i + 1:
            temp = A[A[i] - 1]
            A[A[i] - 1] = A[i]
    for i in range(n):
        if A[i] != i + 1:
            return i + 1
    return n + 1

A = [8,7,6,5,4,3,2,1]
print(find_first_missing_positive(A))