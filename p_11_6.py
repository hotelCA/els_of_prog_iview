def find_number(A, b):
    x, y = len(A) - 1, 0
    while True:
        if A[x][y] == b:
            return True
        elif A[x][y] < b:
            if y == len(A[0]) - 1:
                # We reached the last column
                return False
            y += 1
        else:
            if x == 0:
                # We reached the first row
                return False
            x -= 1

A = [[1,3,7,20,30],
    [4,4,9,25,40],
    [5,7,11,30,50],
    [13,20,21,40,60]]
    
print(find_number(A, 13))