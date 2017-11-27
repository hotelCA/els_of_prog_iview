from p_7_1 import *

def intertwise_list(L):
    if not L:
        return None
    walker = sprinter = L
    while sprinter.next and sprinter.next.next:
        walker = walker.next
        sprinter = sprinter.next.next
    second_half = reverse_list(walker.next)
    walker.next = None
    merge(L, second_half)
    
    return L
    
    
def reverse_list(L):
    point_to = None
    point_from = L
    
    while point_from:
        start_next = point_from.next
        point_from.next = point_to
        point_to = point_from
        point_from = start_next

    return point_to
    
def merge(L1, L2):
    current, next_node = L1, L2
    while current and next_node:
        temp = current.next
        current.next = next_node
        next_node = temp
        current = current.next
        
    
L =  [Node(x) for x in range(11)]
for i in range(len(L) - 1):
    L[i].next = L[i+1]
    
first_half = L[0]
second_half = intertwise_list(L[0])

while first_half:
    print('{}'.format(first_half.value), end = ',')
    first_half = first_half.next
