from p_9_1 import BinaryTreeNode
import collections

Range = collections.namedtuple('Range', ('start', 'end'))

def find_in_interval(tree, interval):
    result = []
    def traverse(root):
        nonlocal interval
        if root is None:
            return
        if root.data >= interval.start and root.data <= interval.end:
            result.append(root.data)
            traverse(root.left)
            traverse(root.right)
        elif root.data < interval.start:
            traverse(root.right)
        else:
            traverse(root.left)
    
    traverse(tree)
    return result
    
tree = [BinaryTreeNode(10),
        BinaryTreeNode(5),
        BinaryTreeNode(15),
        BinaryTreeNode(1),
        BinaryTreeNode(8),
        BinaryTreeNode(11),
        BinaryTreeNode(25),
        BinaryTreeNode(6),
        BinaryTreeNode(13),
        BinaryTreeNode(100),
        BinaryTreeNode(40)]

tree[0].left, tree[0].right = tree[1], tree[2]
tree[1].left, tree[1].right = tree[3], tree[4]
tree[2].left, tree[2].right = tree[5], tree[6]
tree[4].left = tree[7]
tree[5].right = tree[8]
tree[6].right = tree[9]
tree[9].left = tree[10]

print(find_in_interval(tree[0], Range(20, 41)))