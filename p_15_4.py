import math
    
def find_superset(A):
    result = [[]]
    
    def find_individual_sets(B, start):
        for i in range(start, len(A)):
            new_set = []
            if B is None:
                new_set = [A[i]]
            else:
                new_set = B[:]
                new_set.append(A[i])
            result.append(new_set)
            find_individual_sets(new_set, i+1)
            
    find_individual_sets(None, 0)
    return result
    
def find_superset_bitfield(A):
    def get_subsets(bitfield):
        result = []
        while bitfield:
            least_significant_one = bitfield & ~(bitfield-1)
            index = int(math.log2(least_significant_one))
            bitfield &= bitfield-1
            result.append(A[index])
        return result
        
    n = len(A)
    result = []
    for i in range(2**n):
        result.append(get_subsets(i))
        
    return result
    
A = [1,2,3,4]
result_a = find_superset(A)
result_b = find_superset_bitfield(A)
print(result_a)
print(result_b)