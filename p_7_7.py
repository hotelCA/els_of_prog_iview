from p_7_1 import *

def remove_k_last_elements(L, k):
    first = last = L
    count = 0
    while last and count < k:
        count += 1
        if count < k:
            last = last.next
    if not last or not last.next:
        return None
    while last.next:
        last = last.next
        if last.next:
            first = first.next
    first.next = None
    return L

def remove_k_last_elements_2(L, k):
    first = second = dummy = Node(0, L)
    for _ in range(k):
        if not first.next:
            break
        first = first.next

    while first.next:
        first, second = first.next, second.next
    second.next = None
    return dummy.next

L = [Node(x) for x in range(10)]
for i in range(len(L)-1):
    L[i].next = L[i+1]

current = remove_k_last_elements_2(L[0], 2)

while current:
    print('{}'.format(current.value), end=', ')
    current = current.next