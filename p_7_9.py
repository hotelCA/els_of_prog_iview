from p_7_1 import *

def shift_right(L, k):
    first = second = dummy = Node(0, L)
    for _ in range(k):
        if first.next:
            first = first.next
        else:
            first = dummy.next

    if not first.next:
        return L

    while first.next:
        first, second = first.next, second.next

    first.next = dummy.next
    dummy.next = second.next
    second.next = None

    return dummy.next

L = [Node(x) for x in range(10)]
for i in range(len(L)-1):
    L[i].next = L[i+1]

current = shift_right(L[0], 13)

while current:
    print('{}'.format(current.value), end=', ')
    current = current.next