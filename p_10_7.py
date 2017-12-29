import heapq
import collections

StackItem = collections.namedtuple('StackItem', ('index', 'value'))
class Stack:
    def __init__(self):
        self._highest_index = -1
        self._min_heap = []
        
    def push(self, item):
        heapq.heappush(self._min_heap, StackItem(self._highest_index, item))
        self._highest_index -= 1
        
    def pop(self):
        if not self._min_heap:
            raise IndexError('Stack Empty.')
        self._highest_index += 1
        return heapq.heappop(self._min_heap).value
        
    def peek(self):
        if not self._min_heap:
            raise IndexError('Stack Empty.')
        return self._min_heap[0].value
        
            
test_stack = Stack()
test_stack.push(5), print(test_stack.peek())
test_stack.push(7), print(test_stack.peek())
test_stack.push(3), print(test_stack.peek())
test_stack.push(21), print(test_stack.peek())
test_stack.pop(), print(test_stack.peek())
test_stack.pop(), print(test_stack.peek())
test_stack.push(2), print(test_stack.peek())
test_stack.pop(), print(test_stack.peek())
test_stack.pop(), print(test_stack.peek())
test_stack.pop(), print(test_stack.peek())
