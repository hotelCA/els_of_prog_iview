def levenshtein(A, B):
    def compute_levenshtein(a_index, b_index):
        if a_index == -1 or b_index == -1:
            return a_index + 1 + b_index + 1
        elif D[a_index][b_index] != -1:
            return D[a_index][b_index]
        else:
            if A[a_index] == B[b_index]:
                D[a_index][b_index] = compute_levenshtein(a_index-1, b_index-1)
            else:
                D[a_index][b_index] = 1 + min(compute_levenshtein(a_index-1, b_index-1),
                                              compute_levenshtein(a_index, b_index-1),
                                              compute_levenshtein(a_index-1, b_index))
            return D[a_index][b_index]

    D = [[-1] * len(B) for _ in A]
    return compute_levenshtein(len(A)-1, len(B)-1)

A = 'Carthorse'
B = 'Orchestra'
C = 'apples'
D = 'ape'

print(levenshtein(A, B))
print(levenshtein(C, D))