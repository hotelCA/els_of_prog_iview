import sys

def find_closest_dup(A):
    string_lookup_table = {}
    result = (sys.maxsize, 0)
    for i, x in enumerate(A):
        if x in string_lookup_table:
            new_distance = i - string_lookup_table[x]
            if new_distance < result[0]:
                result = (new_distance, i)
        string_lookup_table[x] = i
    return result[1]
    
A = ['A', 'B', 'C', 'A', 'D', 'E', 'Z', 'E', 'F', 'A', 'B', 'E']
print(find_closest_dup(A))