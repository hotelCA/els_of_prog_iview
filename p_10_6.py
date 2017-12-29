import heapq
import collections

HeapNode = collections.namedtuple('HeapNode', ['value', 'index'])

def find_k_largest(A, k):
    heap_size = len(A)
    if heap_size == 0:
        return None
    max_heap = [HeapNode(-A[0], 0)]
    
    while k and max_heap:
        max_node = heapq.heappop(max_heap)
        print(-max_node.value)
        left_index, right_index = (2 * max_node.index) + 1, (2 * max_node.index) + 2
        if left_index < heap_size:
            heapq.heappush(max_heap, HeapNode(-A[left_index], left_index))
        if right_index < heap_size:
            heapq.heappush(max_heap, HeapNode(-A[right_index], right_index))
        k -= 1
    
A = [500,300,400,250,150,200,100,180,90,100,110,170,50]
find_k_largest(A, 7)