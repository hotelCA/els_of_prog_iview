def minimize_wait_time(A):
    A.sort()
    total_wait_time = 0
    for i in range(len(A)-1):
        total_wait_time += (len(A) - 1 - i) * A[i]
    return total_wait_time

A = [4,3,5,2,1,16]
print(minimize_wait_time(A))