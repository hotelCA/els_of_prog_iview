import itertools
import heapq

def concatenate_sorted_lists(L):
    k = len(L)
    min_heap = []
    result = []
    iter_array = [iter(x) for x in L]

    for i, x in enumerate(L):
        item = next(iter_array[i], None)
        heapq.heappush(min_heap, (item, i))

    while min_heap:
        popped_item, index = heapq.heappop(min_heap)
        new_item = next(iter_array[index], None)
        if new_item:
            heapq.heappush(min_heap, (new_item, index))
        result.append(popped_item)

    return result

L = [[1,2,3], [4,5,6,10], [7,8,9]]
print(concatenate_sorted_lists(L))