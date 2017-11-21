def is_a_bst(T, l=float('-inf'), u=float('inf')):
    if not T:
        return True
    else:
        return False if T.data < l or T.data > u else (
            is_a_bst(T.left, l, T.data) and is_a_bst(T.right, T.data, u))
