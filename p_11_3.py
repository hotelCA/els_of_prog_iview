from decorators import time_it

@time_it
def find_smallest_in_cyclic_optimal(A):
    L,  U = 0 , len(A) - 1
    if A[L] <= A[U]:
        return L
    if len(A) == 2:
        return U

    while L < U:
        M = (L + U) // 2
        if A[M] > A[M+1]:
            return M+1
        elif A[M] < A[M-1]:
            return M
        elif A[M] > A[U]:
            L = M + 1
        elif A[M] < A[L]:
            U = M - 1
@time_it
def find_smallest_in_cyclic(A):
    L, U = 0, len(A) - 1
    while L < U:
        M = (L + U) // 2
        if A[M] > A[U]:
            L = M + 1
        elif A[M] < A[U]:
            U = M
    return L


A = [x for x in range(1000000)]
A = A[-10000:] + A[:-10000]
print(find_smallest_in_cyclic(A))
print(find_smallest_in_cyclic_optimal(A))