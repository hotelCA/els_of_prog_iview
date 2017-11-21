def find_iden_item_index(A):
    L = 0
    U = len(A) - 1
    result = -1
    while L <= U:
        M = L + (U - L) // 2
        if A[M] < M:
            L = M + 1
        elif A[M] > M:
            U = M - 1
        else:
            return M

    return result

A = [-1,-2,0,1,3,4,5,6,7,8,10]
print(find_iden_item_index(A))