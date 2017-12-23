from p_9_1 import BinaryTreeNode

def find_kth_element(tree, k):
    if k <= 0 or not tree:
        return None
    
    def traverse(tree, curr_index):
        if not tree:
            return None
        
        left_subtree_size = 0 if not tree.left else tree.left.data
        
        if curr_index + left_subtree_size + 1 == k:
            # Found the k-th node
            return tree
        else:
            # Didn't find the k-th node yet
            if curr_index + left_subtree_size >= k:
                return traverse(tree.left, curr_index)
            else:
                return traverse(tree.right, curr_index + left_subtree_size + 1)
                
    return traverse(tree, 0)

tree = [BinaryTreeNode(0) for _ in range(11)]
tree[0].left, tree[0].right = tree[1], tree[2]
tree[1].left, tree[1].right = tree[3], tree[4]
tree[2].left, tree[2].right = tree[5], tree[6]
tree[5].left, tree[5].right = tree[7], tree[8]
tree[6].left, tree[6].right = tree[9], tree[10]

tree[0].data = 11
tree[1].data = 3
tree[2].data = 7
tree[3].data = 1
tree[4].data = 1
tree[5].data = 3
tree[6].data = 3
tree[7].data = 1
tree[8].data = 1
tree[9].data = 1
tree[10].data = 1

print(find_kth_element(tree[0], 8).data)
        
    
    