from p_9_1 import BinaryTreeNode
from sys import maxsize

def traverse_in_order(root):
    if root is None:
        return
    traverse_in_order(root.left)
    print(root.data)
    traverse_in_order(root.right)
    
def reconstruct_bst(A):
    i = -1
    
    def traverse(lower_bound, upper_bound):
        nonlocal i 
        curr = i + 1
        # print("newnode: {}, LB {}, UB {}".format(A[curr], lower_bound, upper_bound))

        if curr >= len(A) or A[curr] < lower_bound or A[curr] > upper_bound:
            return None
        i = curr
        new_node = BinaryTreeNode(A[i])
        new_node.left = traverse(lower_bound, new_node.data)
        new_node.right = traverse(new_node.data, upper_bound)
        return new_node
        
    return traverse(-maxsize-1, maxsize)
        
A = [50, 40, 20, 30, 25, 35, 90, 70, 200, 150]
root = reconstruct_bst(A)
traverse_in_order(root)
