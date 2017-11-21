def find_next_largest(T, x):
    walker, result = T, None
    while walker:
        if walker <= x:
            walker = walker.right
        else:
            result, walker = walker.data, walker.left
    return result