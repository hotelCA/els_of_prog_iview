class Node:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

def search_list(L, key):
    while L and L.value != key:
        L = L.next
    return L

def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

def remove_after(node):
    if node.next != None:
        node.next = node.next.next

def merge_lists(K1, K2):
    L1, L2 = K1, K2
    if L1 == None:
        return L2
    while L2 != None:
        if L1.next == None or L2.value < L1.next.value:
            insert_after(L1, Node(L2.value))
            L2 = L2.next
        L1 = L1.next
    return K1

l1_array = [Node(1), Node(3), Node(5), Node(6)]
l2_array = [Node(1), Node(2), Node(2), Node(4), Node(6)]

for i in range(len(l1_array)-1):
    l1_array[i].next = l1_array[i+1]

for i in range(len(l2_array)-1):
    l2_array[i].next = l2_array[i+1]

L1 = l1_array[0]
L2 = l2_array[0]

# merged_list = merge_lists(L1, L2)
# walk_ptr = merged_list
#
# while walk_ptr != None:
#     print(str(walk_ptr.value) + ' ')
#     walk_ptr = walk_ptr.next