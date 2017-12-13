from p_9_1 import BinaryTreeNode

def lca_with_parent(node1, node2):
    
    def find_depth(node):
        depth = 0
        while node.parent:
            node = node.parent
            depth += 1
        return depth

    depth1, depth2 = find_depth(node1), find_depth(node2)    
    depth_difference = abs(depth1 - depth2)
    deeper = node1 if depth1 - depth2 >= 0 else node2
    shallower = node1 if depth1 - depth2 < 0 else node2
    
    # Ascend deeper node to the same lever as the shallower node
    while depth_difference > 0:
        deeper = deeper.parent
        depth_difference -= 1
        
    # Ascend nodes in tandem until common node is found. This node is the LCA
    while deeper is not shallower:
        deeper = deeper.parent
        shallower = shallower.parent
        
    return deeper
        
tree = [BinaryTreeNode(i) for i in range(9)]
tree[0].left, tree[0].right = tree[1], tree[2]
tree[1].parent = tree[2].parent = tree[0]

tree[2].left, tree[2].right = tree[3], tree[4]
tree[3].parent = tree[4].parent = tree[2]

tree[3].right = tree[5]
tree[5].parent = tree[3]

tree[4].left, tree[4].right = tree[6], tree[7]
tree[6].parent = tree[7].parent = tree[4]

tree[7].left = tree[8]
tree[8].parent = tree[7]

print(lca_with_parent(tree[8], tree[7]).data)
    