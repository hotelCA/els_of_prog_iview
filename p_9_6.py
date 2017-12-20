from p_9_1 import BinaryTreeNode

def detect_sum(tree, value):
    
    def traverse(tree, running_sum):
        if not tree:
            return False
            
        partial_sum = running_sum + tree.data
        if partial_sum == value:
            return True
        else:
            return(traverse(tree.left, partial_sum) or
                   traverse(tree.right, partial_sum))

    return traverse(tree, 0)
    
tree = [BinaryTreeNode(0) for _ in range(7)]
tree[0].left, tree[0].right = tree[1], tree[2]
tree[2].left, tree[2].right = tree[3], tree[4]
tree[4].left, tree[4].right = tree[5], tree[6]
tree[0].data = 6
tree[1].data = 271
tree[2].data = 561
tree[3].data = 28
tree[4].data = 0
tree[5].data = 3
tree[6].data = 17

print(detect_sum(tree[0], 567))