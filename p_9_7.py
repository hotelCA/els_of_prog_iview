from p_9_1 import BinaryTreeNode

def traverse_in_order_without_recursion(tree):
    if not tree:
        return False
    stack = [tree]
    popped_nodes = set()
    while stack:
        if stack[-1].left and stack[-1].left not in popped_nodes:
            stack.append(stack[-1].left)
        else:
            popped_node = stack.pop()
            print(str(popped_node.data) + ', ', end='')
            popped_nodes.add(popped_node)
            if popped_node.right:
                stack.append(popped_node.right)
                
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

traverse_in_order_without_recursion(tree[0])