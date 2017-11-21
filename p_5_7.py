def buy_stock_twice(A):
    if len(A) < 2:
        return 0
    B = [0] * (len(A) + 1)
    maximum = 0
    for i in reversed(range(len(A)-1)):
        maximum = max(maximum, A[i])
        B[i] = max(B[i+1], maximum-A[i])

    max_sum = 0
    minimum = A[0]

    for i in range(1, len(A)-1):
        minimum = min(minimum, A[i])
        max_sum = max(max_sum, (A[i] - minimum) + B[i+1])

    return max_sum

A = [1,2,0,3,7,5,6,3,4,5,6,3,6,9,4,3,5]
print(buy_stock_twice(A))