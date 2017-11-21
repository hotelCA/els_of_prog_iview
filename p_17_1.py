def divide_labor_efficiently(A):
    A.sort()
    longest = 0
    for i in range(len(A)//2):
        duration = A[i] + A[~i]
        if duration > longest:
            longest = duration
    return longest

A = [5,2,1,6,4,4]
print(divide_labor_efficiently(A))
print(~5)