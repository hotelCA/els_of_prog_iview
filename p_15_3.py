def find_all_permutations(A):

    def next_item(A, remaining_items):
        if len(remaining_items) == 1:
            result.append(A + [remaining_items[0]])
        else:
            for i in range(len(remaining_items)):
                next_item(A + [remaining_items[i]], remaining_items[:i] + remaining_items[i+1:])

    result = []
    next_item(list(), A)
    return result

A = ['a','b','c','d','e']
result = find_all_permutations(A)
# print(result)
print(len(result))