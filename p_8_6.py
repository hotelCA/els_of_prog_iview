def get_sunset_view(L):
    stack = [L[0]]
    i = 1
    while i < len(L):
        if stack and stack[-1] <= L[i]:
            stack.pop()
        else:
            stack.append(L[i])
            i += 1
    return stack

L = [5,3,2,4,2,3,2,1]
L = [1,2,6,4,5]
print(get_sunset_view(L))