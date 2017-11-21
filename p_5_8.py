def alternate_array(A):
    for i in range(len(A)-1):
        if i % 2 == 0:
            A[i], A[i+1] = min(A[i], A[i+1]), max(A[i], A[i+1])
        else:
            A[i], A[i+1] = max(A[i], A[i+1]), min(A[i], A[i+1])

A = [5,1,3,2,7,6,5,5,4,1,3]
alternate_array(A)
print(A)