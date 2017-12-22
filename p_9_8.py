from p_9_1 import BinaryTreeNode

def traverse_preorder(tree):
    stack = [tree]
    while stack:
        popped_node = stack.pop()
        if popped_node:
            print(popped_node.data, end=', ')
            stack += [popped_node.right, popped_node.left]
            
tree = [BinaryTreeNode(0) for _ in range(9)]
tree[0].left, tree[0].right = tree[1], tree[2]
tree[2].left, tree[2].right = tree[3], tree[4]
tree[4].left, tree[4].right = tree[5], tree[6]
tree[1].left = tree[7]
tree[7].right = tree[8]
tree[0].data = 6
tree[1].data = 271
tree[2].data = 561
tree[3].data = 28
tree[4].data = 0
tree[5].data = 3
tree[6].data = 17
tree[7].data = 0
tree[8].data = 5

traverse_preorder(tree[0])
        
    