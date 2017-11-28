from p_9_1 import BinaryTreeNode


class BinaryTreeNodeWithColor(BinaryTreeNode):
    def __init__(self, data=None):
        BinaryTreeNode.__init__(self, data)
        self.color = 0


def post_order(T):
    if not T:
        return
    my_stack = [T]

    while True:
        head = my_stack[-1]
        if (head.left and head.left.color == 0) or (head.right and head.right.color == 0):
            if head.right and head.right.color == 0:
                my_stack.append(head.right)
            if head.left and head.left.color == 0:
                my_stack.append(head.left)
        else:
            x = my_stack.pop()
            x.color = 1
            print(x.data)
            if not my_stack:
                break


nodes = [BinaryTreeNodeWithColor(i) for i in range(5)]
nodes[0].left, nodes[0].right = nodes[1], nodes[2]
nodes[2].left, nodes[2].right = nodes[3], nodes[4]


post_order(nodes[0])  # should print 1, 3, 4, 2, 0
