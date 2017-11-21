from p_7_1 import *

def delete_node(x):
    x.value = x.next.value
    temp = x.next
    x.next = x.next.next
    temp.next = None

L = [Node(x) for x in range(10)]
for i in range(len(L)-1):
    L[i].next = L[i+1]

delete_node(L[3])
current = L[0]
while current:
    print('{}'.format(current.value), end=', ')
    current = current.next