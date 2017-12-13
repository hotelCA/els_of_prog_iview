from p_9_1 import BinaryTreeNode

def least_common_ancestors(tree, node1, node2):
    lca = None
    def traverse(tree):
        nonlocal lca
        if not tree:
            return 0
        left_subtree = traverse(tree.left)
        right_subtree = traverse(tree.right)
        
        if left_subtree == 1 and right_subtree == 1:
            # each node comes from a separate subtree
            lca = tree
            return 0
        elif left_subtree == 2 or right_subtree == 2:
            lca = tree
            return 0
        elif (tree.data == node1.data) or (tree.data == node2.data):
            # One node is ancestor of the other
            if left_subtree or right_subtree:
                return 2
            else:
                return 1
        return left_subtree or right_subtree
        
    traverse(tree)
    return lca

tree = [BinaryTreeNode(i) for i in range(9)]
tree[0].left, tree[0].right = tree[1], tree[2]
tree[2].left, tree[2].right = tree[3], tree[4]
tree[3].right = tree[5]
tree[4].left, tree[4].right = tree[6], tree[7]
tree[7].left = tree[8]
print(least_common_ancestors(tree[0], tree[8], tree[7]).data)
