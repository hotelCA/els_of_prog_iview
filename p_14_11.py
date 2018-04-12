from p_9_1 import BinaryTreeNode


def proper_threesome(n_1, n_2, m):
    if n_1.data == m.data or n_2.data == m.data or n_1.data == n_2.data:
        return False
        
    t_1, t_2 = n_1, n_2
    descendant = n_1
    
    while t_1 or t_2:
        # print("t1: {}, t2: {}".format(t_1.data, t_2.data))
        if t_1 is not None:
            t_1 = t_1.left if t_1.data > m.data else t_1.right
            if t_1 == m:
                descendant = n_2
                break
        if t_2 is not None:
            t_2 = t_2.left if t_2.data > m.data else t_2.right
            if t_2 == m:
                break
        
    if t_1 or t_2:
        while m:
            print("m: {}, desc: {}".format(m.data, descendant.data))
            if m.data < descendant.data:
                m = m.right
            elif m.data > descendant.data:
                m = m.left
            else:
                return True
    return False

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

print(proper_threesome(tree[0], tree[10], tree[6]))