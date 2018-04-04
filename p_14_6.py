from p_9_1 import BinaryTreeNode
from p_14_5 import traverse_in_order

class BTNwithIndex(BinaryTreeNode):
    def __init__(self, data=None, left=None, right=None, parent=None, index=0):
       BinaryTreeNode.__init__(self, data, left, right, parent)
       self.index = index

def init_tree(A):
    root = BTNwithIndex(data=A[0][0], index = 0)
    for i in range(1, len(A)):
        insert(root, A[i][0], i)
    return root

def insert(root, node_data, i):
    new_node = BTNwithIndex(data=node_data, index=i)
    # print("Insert | data: {}, i: {}".format(new_node.data, new_node.index))

    if root is None:
        return new_node
    curr = root
    while True:
        if node_data >= curr.data:
            if curr.right:
                curr = curr.right
            else:
                curr.right = new_node
                break
        else:
            if curr.left:
                curr = curr.left
            else:
                curr.left = new_node
                break
        
def calc_interval(root):
    curr = root
    while curr.left:
        curr = curr.left
    smallest = curr.data
    curr = root
    while curr.right:
        curr = curr.right
    print("Interval: {}".format(curr.data - smallest))
    return curr.data - smallest

def remove_min(root):
    # print("before")
    # traverse_in_order(root)
    parent = root
    ret_node = root.left
    if ret_node is None:
        ret_node = root
        root = root.right
    else:
        while ret_node.left:
            parent = ret_node
            ret_node = ret_node.left
        parent.left = ret_node.right
    ret_node.right = None

    # print("after")
    # traverse_in_order(root)
    return ret_node, root
    
def find_min_interval(A):
    if len(A) < 2:
        return 0
    tree = init_tree(A)
    cursors = [1] * len(A)
    min_interval = calc_interval(tree)
    
    while True:
        removed, tree = remove_min(tree)

        subarray_index = removed.index
        # print(subarray_index)
        if cursors[subarray_index] == len(A[subarray_index]):
            break
        # print("before insert")
        # traverse_in_order(tree)
        insert(tree, A[subarray_index][cursors[subarray_index]], subarray_index)
        # print("after insert")
        # traverse_in_order(tree)
        cursors[subarray_index] += 1
        min_interval = min(min_interval, calc_interval(tree))
    
    return min_interval
        
A = [[2,3,4,5,21],
     [1,5,10,15,20,25],
     [10,18,22,26,30]]
     
print("result is {}".format(find_min_interval(A)))