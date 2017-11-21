def remove_duplicate(A):
    A.sort()
    last_item = 1
    for x in A[1:]:
        if x != A[last_item-1]:
            A[last_item] = x
            last_item += 1
    del A[last_item:]


A = [5,4,3,6,87,5,3,3,4,4,4,3,3,5,1,100,6,7,8,9,7,7,6,5,5,4,-22,-23]
B = [1,2,3,4,5,6]
remove_duplicate(A)
remove_duplicate(B)
print(A)
print(B)