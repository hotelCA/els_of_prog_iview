def max_distinct_subset(A):
    
    substring = set()
    head = tail = 0
    result = (0, 0)

    while True:
        # Moving tail forward
        while (tail < len(A)) and (A[tail] not in substring):
            substring.add(A[tail])
            tail += 1

        # Compare current subset with the previous best subset
        print('head: {}, tail: {}'.format(head, tail))
        
        if ((tail-1) - head) > (result[1] - result[0]):
            result = (head, tail-1)
            
        # Check for the end of array
        if tail == len(A):
            break
            
        # Moving head forward
        while A[tail] in substring:
            substring.remove(A[head])
            head += 1
            
    return result
    
A = ['A', 'B', 'G', 'C', 'D', 'E', 'E', 'G', 'F', 'A', 'B', 'Z']

print(max_distinct_subset(A))