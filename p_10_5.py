import heapq

def find_running_median(S):
    min_heap, max_heap = [], []
    for x in S:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        if len(max_heap) > len(min_heap):
            print(-max_heap[0])
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        else:
            print(0.5 * (-max_heap[0] + min_heap[0]))
            
S = [0,5,7,2,1,8,3,4,5]
find_running_median(S)