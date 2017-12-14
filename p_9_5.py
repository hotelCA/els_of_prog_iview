from p_9_1 import BinaryTreeNode

def sum_leaf_paths(tree):
    if not tree:
        return 0
    
    sum = 0
    def traverse(tree, running_sum):
        nonlocal sum
        running_sum_plus_current = (running_sum << 1) + tree.data
        if not tree.left and not tree.right:
            # At leaf node. Update sum
            sum += running_sum_plus_current
        else:
            if tree.left:
                traverse(tree.left, running_sum_plus_current)
            if tree.right:
                traverse(tree.right, running_sum_plus_current)
    traverse(tree, 0)
    return sum
    
tree = [BinaryTreeNode(1) for _ in range(7)]
tree[2].data = tree[6].data = 0
tree[0].left, tree[0].right = tree[1], tree[2]
tree[2].left, tree[2].right = tree[3], tree[4]
tree[4].left, tree[4].right = tree[5], tree[6]

print(sum_leaf_paths(tree[0]))