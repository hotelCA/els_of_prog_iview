from p_9_1 import BinaryTreeNode
import heapq


class MostVisitedPages:
    def __init__(self, k):
        self.page_visit_count = dict()
        self.min_heap = []
        self.k = k

    def push(self, min_heap, l):
        min_heap.append(l)
        i = len(min_heap) - 1
        parent = (i - 1) // 2
        while parent >= 0 and self.page_visit_count[min_heap[i]][0] < self.page_visit_count[min_heap[parent]][0]:
            min_heap[i], min_heap[parent] = min_heap[parent], min_heap[i]
            i, parent = parent, (parent - 1) // 2
                    
    def pop(self, min_heap):
        popped_item = min_heap[0]
        min_heap[0] = min_heap[-1]
        del min_heap[-1]
        i = 0
        left_child, right_child = 2 * i + 1, 2 * i + 2
        smaller_child = left_child
        if right_child < len(min_heap):
            if self.page_visit_count[min_heap[right_child]][0] < self.page_visit_count[min_heap[left_child]][0]:
                smaller_child = right_child

        while smaller_child < len(min_heap) and self.page_visit_count[min_heap[i]][0] > self.page_visit_count[min_heap[smaller_child]][0]:
            min_heap[i], min_heap[smaller_child] = min_heap[smaller_child], min_heap[i]
            i = smaller_child
            left_child, right_child = 2 * i + 1, 2 * i + 2
            smaller_child = left_child
            if right_child < len(min_heap):
                if self.page_visit_count[min_heap[right_child]][0] < self.page_visit_count[min_heap[left_child]][0]:
                    smaller_child = right_child
        return popped_item
        
    def read_line(self, l):
        if l not in self.page_visit_count:
            self.page_visit_count[l] = [1, False]
            if len(self.min_heap) < self.k:
                self.push(self.min_heap, l)
                self.page_visit_count[l][1] = True
        else:
            self.page_visit_count[l][0] += 1
            already_in_heap = self.page_visit_count[l][1]
            # print('{}: {}, in heap = {}, min item {}'.format(l, self.page_visit_count[l][0], already_in_heap, self.min_heap[0]))
            if not already_in_heap and self.page_visit_count[l][0] > self.page_visit_count[self.min_heap[0]][0]:
                # print("Push {}".format(l))
                popped_item = self.pop(self.min_heap)
                self.page_visit_count[popped_item][1] = False
                self.push(self.min_heap, l)
                self.page_visit_count[l][1] = True
                
    def print_mvp(self):
        for x in self.min_heap:
            print('{}: {}'.format(x, self.page_visit_count[x]))

lines = [1,2,3,4,5,2,3,4,3,2,4,5,6,7,6,5,6,1,4,3,6,3,4,5,6,4,4,3,2,3,3,4,3]
line_hash = dict()
for l in lines:
    if l not in line_hash:
        line_hash[l] = 1
    else:
        line_hash[l] += 1
        
for key, value in line_hash.items():
    print(key, value)
    
mvp = MostVisitedPages(3)
for l in lines:
    mvp.read_line(l)
    
mvp.print_mvp()
        
                
        