from p_9_1 import BinaryTreeNode


class BinaryTreeNodeWithColor(BinaryTreeNode):
    def __init__(self, data=None):
        BinaryTreeNode.__init__(self, data)
        self.color = 0


def post_order(T):
    if not T:
        return
    my_stack = [T]
    last_popped = None

    while True:
        head = my_stack[-1]
        if (head.left or head.right) and \
                not ((head.left and last_popped == head.left.data) or (head.right and last_popped == head.right.data)):
            if head.right:
                my_stack.append(head.right)
            if head.left:
                my_stack.append(head.left)
        else:
            x = my_stack.pop()
            last_popped = x.data
            print(x.data)
            if not my_stack:
                break


nodes = [BinaryTreeNode(i) for i in range(8)]
nodes[0].left, nodes[0].right = nodes[1], nodes[2]
nodes[2].left, nodes[2].right = nodes[3], nodes[4]
nodes[1].right = nodes[7]
nodes[3].left = nodes[5]
nodes[4].right = nodes[6]


post_order(nodes[0])  # should print 7,1,5,3,6,4,2,0
