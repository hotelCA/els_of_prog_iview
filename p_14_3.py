from p_9_1 import BinaryTreeNode

def find_k_largest(root, k):
    
    def in_order_backwards(root):
        if root is None:
            return
        
        in_order_backwards(root.right)
        if len(result) == k:
            return
        result.append(root.data)
        in_order_backwards(root.left)
    
    result = []
    in_order_backwards(root)
    return result
    
tree = [BinaryTreeNode(10),
        BinaryTreeNode(5),
        BinaryTreeNode(15),
        BinaryTreeNode(1),
        BinaryTreeNode(8),
        BinaryTreeNode(11),
        BinaryTreeNode(25),
        BinaryTreeNode(6),
        BinaryTreeNode(13),
        BinaryTreeNode(100),
        BinaryTreeNode(40)]

tree[0].left, tree[0].right = tree[1], tree[2]
tree[1].left, tree[1].right = tree[3], tree[4]
tree[2].left, tree[2].right = tree[5], tree[6]
tree[4].left = tree[7]
tree[5].right = tree[8]
tree[6].right = tree[9]
tree[9].left = tree[10]

result = find_k_largest(tree[0], 5)
print(result)


    
    