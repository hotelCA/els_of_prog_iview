from p_9_1 import BinaryTreeNode

def find_sum(tree):
    if not tree:
        return 0
    sum  = 0
    
    def traverse(tree, running_sum):
        nonlocal sum
        partial_sum = (running_sum << 1) + tree.data
        if not tree.left and not tree.right:
            sum += partial_sum
        else:
            if tree.left:
                traverse(tree.left, partial_sum)
            if tree.right:
                traverse(tree.right, partial_sum)
    traverse(tree, 0)
    return sum
    
tree = [BinaryTreeNode(0) for _ in range(7)]
tree[0].left, tree[0].right = tree[1], tree[2]
tree[2].left, tree[2].right = tree[3], tree[4]
tree[4].left, tree[4].right = tree[5], tree[6]
tree[0].data = tree[1].data = tree[3].data = tree[5].data = 1
tree[4].data = 1

print(find_sum(tree[0]))
    
    
    