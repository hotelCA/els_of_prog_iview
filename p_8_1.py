import collections

# class Stack:
#
#     ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))
#
#     def __init__(self):
#         self._element_with_cached_max = []
#
#     def is_empty(self):
#         return len(self._element_with_cached_max) == 0
#
#     def max(self):
#         if self.is_empty():
#             raise IndexError('max(): Empty stack')
#         return self._element_with_cached_max[-1].max
#
#     def push(self, x):
#         self._element_with_cached_max.append(self.ElementWithCachedMax(x, x if self.is_empty() else max(self.max(), x)))
#
#     def pop(self):
#         if self.is_empty():
#             raise IndexError('pop(): Empty stack')
#         return self._element_with_cached_max.pop().element

class Stack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def is_empty(self):
        return len(self.max_stack) == 0

    def max(self):
        if self.is_empty():
            raise IndexError('max(): Empty stack')
        return self.max_stack[-1][0]

    def push(self, x):
        self.stack.append(x)
        if self.is_empty() or self.max() < x:
            self.max_stack.append([x, 1])
        else:
            self.max_stack[-1][1] += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('pop(): Empty stack')
        self.stack.pop()

        if self.max_stack[-1][1] == 1:
            self.max_stack.pop()
        else:
            self.max_stack[-1][1] -= 1


test_stack = Stack()
test_stack.push(1)
test_stack.push(2)
test_stack.push(2)
test_stack.push(5)
test_stack.push(5)
test_stack.push(4)
test_stack.push(6)
print(test_stack.max())
test_stack.pop()
print(test_stack.max())
test_stack.pop()
print(test_stack.max())
test_stack.pop()
print(test_stack.max())
test_stack.pop()
print(test_stack.max())
test_stack.pop()
test_stack.push(7)
print(test_stack.max())
test_stack.push(2)
print(test_stack.max())
test_stack.pop()
print(test_stack.max())
test_stack.pop()
print(test_stack.max())


