from p_9_1 import BinaryTreeNode

def find_lca(root, node_1, node_2):
    
    def traverse(root):
        # assuming the two nodes exist in the tree
        if root.data <= larger.data and root.data >= smaller.data:
            return root
        elif root.data < smaller.data:
            return traverse(root.right)
        else:
            return traverse(root.left)
            
    larger = node_2 if node_2.data > node_1.data else node_1
    smaller = node_1 if node_1.data < node_2.data else node_2
    
    return traverse(root)
    
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

print(find_lca(tree[0], tree[3], tree[7]).data)