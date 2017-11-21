from p_7_1 import *

def find_first_common_node(L1, L2):
    l1_len, l2_len = get_len(L1), get_len(L2)
    diff = l1_len - l2_len

    for i in range(abs(diff)):
        if diff > 0:
            L1 = L1.next
        else:
            L2 = L2.next

    while L1 and L2:
        if L1 == L2:
            return L1
        L1, L2 = L1.next, L2.next

    return Node(-1)


def get_len(L):
    count = 0
    while L:
        count += 1
        L = L.next
    return count

L1 = [Node(x) for x in range(10)]
L2 = [Node(x) for x in range(20, 23)]
for i in range(len(L1)-1):
    L1[i].next = L1[i+1]
for i in range(len(L2)-1):
    L2[i].next = L2[i+1]
L2[-1].next = L1[6]
# for x in L1:
#     print('{}, '.format(x.value), end='')
#
# print('')
#
# current = L2[0]
# while current:
#     print('{}, '.format(current.value), end='')
#     current = current.next
# print('')

print(find_first_common_node(L1[0], L2[0]).value)