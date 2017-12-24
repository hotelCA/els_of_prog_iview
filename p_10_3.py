import heapq

def sort_k_sorted_array(A, k):
    # Special cases
    if len(A) <= k:
        return A.sort()
    
    # Init
    min_heap = A[:k]
    heapq.heapify(min_heap)
    print(min_heap)
    
    # Sort first size(A) - k elements
    for i in range(k, len(A)):
        A[i-k] = heapq.heapreplace(min_heap, A[i])
    
    # Sort the remaining k elements
    for i in range(0, k):
        A[len(A) - k + i] = heapq.heappop(min_heap)

A = [1,4,2,3,6,7,5,9,8]
sort_k_sorted_array(A, 3);
print(A)
        