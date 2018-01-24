from p_9_1 import BinaryTreeNode

def find_LCA(n_1, n_2):
    anc_1, anc_2 = set(), set()
    
    while n_1 or n_2:
        if n_1:
            anc_1.add(n_1)
        if n_2:
            anc_2.add(n_2)
        if n_1 in anc_2:
            return n_1
        if n_2 in anc_1:
            return n_2
        n_1 = n_1.parent if n_1 else None
        n_2 = n_2.parent if n_2 else None
    raise ValueError('The two nodes are not from the same tree')
        
tree = [BinaryTreeNode(i) for i in range(0, 9)]
tree[0].left, tree[0].right = tree[1], tree[2]
tree[1].parent = tree[2].parent = tree[0]
tree[1].left, tree[1].right = tree[3], tree[4]
tree[3].parent = tree[4].parent = tree[1]
tree[2].left, tree[2].right = tree[5], tree[6]
tree[5].parent = tree[6].parent = tree[2]
tree[3].left, tree[3].right = tree[7], tree[8]
tree[7].parent = tree[8].parent = tree[3]

print(find_LCA(tree[7], tree[0]).data)
