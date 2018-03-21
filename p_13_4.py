def find_min_nonconstructible(A):
    sum = 0
    for x in sorted(A):
        if x > sum + 1:
            return sum + 1
        else:
            sum += x
    return sum + 1


A = [1,2,3]

print(find_min_nonconstructible(A))
