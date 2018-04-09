from p_9_1 import BinaryTreeNode

def build_min_height_bst(A):
    def build_node(l,u):
        if l > u:
            return None
        pivot = l + (u-l)//2
        new_node = BinaryTreeNode(A[pivot])
        new_node.left = build_node(l, pivot-1)
        new_node.right = build_node(pivot+1, u)
        return new_node
        
    return build_node(0, len(A) - 1)

def print_nodes(root, height):
    if root is None:
        return
    print_nodes(root.left, height + 1)
    print(root.data, height)
    print_nodes(root.right, height + 1)

    
A = [1,2,3,4,5,6,7,8,9,10]
print_nodes(build_min_height_bst(A),0)
