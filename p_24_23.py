from p_9_1 import BinaryTreeNode

def convert_bst_to_doubly_ll(root):
    if not root:
        return
    prev = [None]
    head = [None]
    def traverse(root):
        if not root:
            return
        traverse(root.left)
        process(root)
        traverse(root.right)
    def process(root):
        root.left = prev[0]
        if not head[0]:
            head[0] = root
        else:
            prev[0].right = root
        prev[0] = root

    traverse(root)
    prev[0].right = None
    return head[0]
    
bst = [BinaryTreeNode() for x in range(10)]
bst[0].data = 3
bst[1].data = 7
bst[2].data = 10
bst[3].data = 15
bst[4].data = 16
bst[5].data = 5
bst[6].data = 8
bst[7].data = 19
bst[8].data = 20

bst[0].right = bst[5]
bst[1].left = bst[0]
bst[1].right = bst[3]
bst[2].left = bst[6]
bst[3].left = bst[2]
bst[3].right = bst[4]
bst[4].right = bst[7]
bst[7].right = bst[8]

root = convert_bst_to_doubly_ll(bst[1])
tail = root
while root:
    print('{}'.format(root.data), end=', ')
    root = root.right
    if root:
        tail = root

print()

while tail:
    print('{}'.format(tail.data), end=', ')
    tail = tail.left
    
