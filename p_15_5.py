# def find_k_size_sets(A, k):
    
#     def find_subsets(subset, k):
#         result = []
        
#         if k == 0:
#             return []
#         elif len(subset) == k:
#             return subset
#         else:
#             result.append(find_subsets(subset[1:], k))
#             temp = find_subsets(subset[1:], k-1)
#             for x in temp:
#                 result.append(x.append(subset[0]))
            
#         return result
        
#     result = []
#     for i in range(len(A)):
#         result.append(find_subsets(A[:i] + A[i+1:], k))
        
#     return result

def combinations(n, k):
    def directed_combinations(offset, partial_combination):
        print("offset: {}, partial_combination: {}".format(offset, partial_combination))
        if len(partial_combination) == k:
            result.append(list(partial_combination))
            return
        
        num_remaining = k - len(partial_combination)
        i = offset
        print("remaining: {}".format(num_remaining))

        while i <= n and num_remaining <= n - i + 1:
            print("i: {}".format(i))
            directed_combinations(i+1, partial_combination + [i])
            i += 1
    result = []
    directed_combinations(1, [])
    return result
        
A = [1,2,3,4]

result = combinations(4, 2)
print(result)