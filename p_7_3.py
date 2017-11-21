from p_7_1 import *

def find_cycle(L):

    fast = slow = L

    while fast and slow:
        fast = fast.next
        if fast:
            fast = fast.next
        slow = slow.next
        if slow == fast:
            break
    if not fast:
        return Node(-1)

    slow_2 = fast
    slow = L
    while slow != slow_2:
        slow, slow_2 = slow.next, slow_2.next

    return slow

L = [Node(x) for x in range(10)]
for i in range(len(L)-1):
    L[i].next = L[i+1]
L[-1].next = L[7]

print(find_cycle(L[0]).value)
