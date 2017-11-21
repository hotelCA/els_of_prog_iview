

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def test_height_balanced(root):

    result = traverse(root)
    if result is None:
        return False
    else:
        return True

def traverse(root):
    if root:
        left = traverse(root.left)
        right = None if left is None else traverse(root.right)
        print('left: {}, right: {}'.format(left, right))
        return None if right is None or abs(right-left) > 1 else 1 + max(left, right)
    else:
        return 0

        def largest_complete_tree(root):

            result = traverse_complete(root)
            print('largest complete subtree: {}'.format(result[0]))

        def traverse_complete(root):
            if root:
                left = traverse_complete(root.left)
                right = traverse_complete(root.right)
                max_complete = max(left[0], right[0])
                max_height = max(left[1], right[1])
                left_child_only = 1 if (left[2] == 1 and right[0] == 0) or (left[0] == 1 and right[0] == 0) else 0

                # 5 conditions need to pass before left and right can be joined by this node
                # to create a complete subtree.
                if left[0] < right[0]:
                    return [max_complete, 0, 2]
                if left[2] == 2 or right[2] == 2:
                    return [max_complete, 0, 2]
                if abs(left[1]-right[1]) > 1:
                    return [max_complete, 0, 2]
                if (left[2] == 1 and right[2] == 1) or (left[2] == 0 and right[2] == 1):
                    return [max_complete, 0, 2]
                if left[0] == right[0] and left[0] != 2**left[0] - 1:
                    return [max_complete, 0, 2]
                return [left[0] + right[0] + 1, max_height + 1, left_child_only]
            else:
                return [0,0,0]

# root = BinaryTreeNode()
# nodes = [BinaryTreeNode() for i in range(10)]
#
# root.left, root.right = nodes[0], nodes[1]
# nodes[0].left, nodes[0].right = nodes[2], nodes[3]
# nodes[2].left, nodes[2].right = nodes[4], nodes[5]
# nodes[1].left = nodes[6]
# nodes[1].right = nodes[7]
# nodes[4].left, nodes[4].right = nodes[6], nodes[7]

# nodes[6].right = nodes[7]
# nodes[1].left, nodes[1].right = nodes[8], nodes[9]

# print(test_height_balanced(root))
# print(largest_complete_tree(root))

