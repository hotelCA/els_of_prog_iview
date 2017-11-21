from p_7_1 import *

def remove_dups(L):
    current = L
    if not current:
        return None
    while current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return L

L = [Node(x) for x in range(10)]
for i in range(len(L)-1):
    L[i].next = L[i+1]
L[6].value = 5
L[7].value = 5
L[3].value = 2

current = remove_dups(L[0])

while current:
    print('{}'.format(current.value), end=', ')
    current = current.next