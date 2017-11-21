from p_7_1 import *

def reverse_sublist(L, s, f):
    dummy = sub_header = Node(0, L)
    for i in range(1, s):
        sub_header = sub_header.next

    iter = sub_header.next

    for _ in range(f-s):
        temp = iter.next
        iter.next = temp.next
        temp.next = sub_header.next
        sub_header.next = temp

    return dummy.next

def reverse_sublist_var2(L, k, l):
    dummy = alt_head_1 = Node(0, L)
    moving_head = L
    
    for j in range(l//k):
        iterator = moving_head

        if j % 2 == 0:
            alt_head_2 = iterator
        else:
            alt_head_1 = iterator

        for i in range(1,k):
            temp = iterator.next
            iterator.next = temp.next
            temp.next = moving_head
            moving_head = temp

        moving_head = iterator.next

        if j % 2 != 0:
            alt_head_2.next = temp
        else:
            alt_head_1.next = temp

    return dummy.next

l = [Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8), Node(9), Node(10), Node(11)]
for i in range(len(l)-1):
    l[i].next = l[i+1]
L = l[0]

# walk_ptr = reverse_sublist(L, 2, 7)
walk_ptr = reverse_sublist_var2(L, 4, len(l))

while walk_ptr != None:
    print(str(walk_ptr.value) + ' ')
    walk_ptr = walk_ptr.next
