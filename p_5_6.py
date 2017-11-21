def sell_stock_once(A):
    if not A:
        return 0
    max, buy_index = 0, 1
    for i in range(1, len(A)):
        diff = A[i] - A[buy_index]
        if diff > max:
            max = diff
        elif diff < 0:
            buy_index = i
    return max

A = [5,6,7,6,9,4,6,7,8,7,8,6,10]
print(sell_stock_once(A))