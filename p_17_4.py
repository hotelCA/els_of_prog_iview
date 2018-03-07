def threesome(A, sum):
    A.sort()
    print(A)
    return any(twosum(A, sum - a) for a in A)


def twosum(A, sum):
    i, j = 0, len(A) - 1
    while i <= j:
        if A[i] + A[j] == sum:
            return True
        elif A[i] + A[j] < sum:
            i += 1
        else:
            j -= 1

    return False

A = [6,2,7,4,1,9,5]
print(threesome(A, 26))
