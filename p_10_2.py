import heapq
import itertools

def sort_incr_decr_array(L):
    if len(L) <= 1:
        return L
    increasing = True if L[1] >= L[0] else False
    sequences = [[L[0], L[1]]]
    for i in range(2, len(L)):
        if L[i] < L[i-1] and increasing:
            sequences.append([L[i]])
            increasing = False
        elif L[i] > L[i-1] and not increasing:
            sequences[-1].reverse()
            sequences.append([L[i]])
            increasing = True
        else:
            sequences[-1].append(L[i])
    if not increasing:
        sequences[-1].reverse()
    return sort_sorted_sequences(sequences)

def sort_sorted_sequences(S):
    result, min_heap = [], []
    iter_array = [iter(s) for s in S]

    for i, iterator in enumerate(iter_array):
        first_item = next(iterator, None)
        if first_item:
            heapq.heappush(min_heap, (first_item, i))

    while min_heap:
        min_item = heapq.heappop(min_heap)
        data, sequence_index = min_item
        result.append(data)
        next_heap_item = next(iter_array[sequence_index], None)
        if next_heap_item:
            heapq.heappush(min_heap, (next_heap_item, sequence_index))
    return result


L = [15,10,7,1,2,3,9,20,26,19,17,14]
# L = [3,2,1,1,2,3,3,2,1]

print(sort_incr_decr_array(L))

class Monotonic:
    def __init__(self):
        self._last = float('-inf')

    def __call__(self, curr):
        res = curr < self._last
        print(res)
        self._last = curr
        return res


L = [list(group)[::-1 if is_decreasing else 1] for is_decreasing, group in itertools.groupby(L, Monotonic())]
print(L)