from p_9_1 import BinaryTreeNode

def is_mirrored(root):
    return compare(root.left, root.right)

def compare(subtree_0, subtree_1):
    if subtree_0 is None and subtree_1 is None:
        return True
    elif subtree_0 is None or subtree_1 is None or subtree_0.data != subtree_1.data:
        return False
    else:
        return compare(subtree_0.left, subtree_1.right) and compare(subtree_0.right, subtree_1.left)


root = BinaryTreeNode()
nodes = [BinaryTreeNode() for i in range(10)]

root.left, root.right = nodes[0], nodes[1]
nodes[0].right, nodes[2].left = nodes[2], nodes[3]
nodes[1].left, nodes[4].right = nodes[4], nodes[5]
nodes[0].data, nodes[1].data = 1, 1
nodes[2].data, nodes[4].data = 2, 2
nodes[3].data, nodes[5].data = 3, 3
nodes[5].right = nodes[6]
nodes[6].data = 4

print(is_mirrored(root))