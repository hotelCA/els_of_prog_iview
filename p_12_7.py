import sys

def find_smallest_subset(A, S):
    character_positions = []
    for i, x in enumerate(A):
        if x in S:
            character_positions.append((i, x))
    
    subset_character_count = {}
    head = tail = 0
    result = (0, sys.maxsize)
    
    while True:
        # Moving tail forward
        while (len(subset_character_count) < len(S)) and (tail < len(character_positions)):
            curr = character_positions[tail][1]
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
            curr = character_positions[head][1]
            subset_character_count[curr] -= 1
            if subset_character_count[curr] == 0:
                del subset_character_count[curr]
            head += 1

        # Compare current subset with the previous best subset
        print('head: {}, tail: {}'.format(head, tail))
        start_index, end_index = character_positions[head-1][0], character_positions[tail-1][0]
        if (end_index - start_index) < (result[1] - result[0]):
            result = (start_index, end_index)
            
    return result
    
A = ['A', 'B', 'A', 'C', 'D', 'E', 'E', 'E', 'F', 'A', 'B', 'E']
S = set(['E', 'A'])

print(find_smallest_subset(A, S))