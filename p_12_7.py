import sys

def find_smallest_subset(A, S):
    
    subset_character_count = {}
    head = tail = 0
    result = (0, sys.maxsize)
    
    while True:
        # Moving tail forward
        while (len(subset_character_count) < len(S)) and (tail < len(A)):
            curr = A[tail]
            if curr in S:
                if curr not in subset_character_count:
                    subset_character_count[curr] = 1
                else:
                    subset_character_count[curr] += 1
            tail += 1
            
        # Check for the end of array
        if len(subset_character_count) < len(S):
            break
            
        # Moving head forward
        while (len(subset_character_count) == len(S)) and (head < tail):
            curr = A[head]
            if curr in S:
                subset_character_count[curr] -= 1
                if subset_character_count[curr] == 0:
                    del subset_character_count[curr]
            head += 1

        # Compare current subset with the previous best subset
        print('head: {}, tail: {}'.format(head, tail))
        if (tail - head) < (result[1] - result[0]):
            result = (head, tail)
            
    # Adjust result
    return (result[0] - 1, result[1] - 1)
    
A = ['A', 'B', 'A', 'C', 'D', 'E', 'E', 'E', 'F', 'A', 'B', 'E']
S = set(['E', 'D', 'F'])

print(find_smallest_subset(A, S))