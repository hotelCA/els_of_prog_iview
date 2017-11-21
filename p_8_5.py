class JumpNode:
    def __init__(self, jump=None, next=None):
        self.value = -1
        self.jump = jump
        self.next = next

def get_jump_order(L):
    def jump_order_helper(current):
        if current and current.value == -1:
            current.value = order[0]
            order[0] += 1
            jump_order_helper(current.jump)
            jump_order_helper(current.next)

    order = [0]
    jump_order_helper(L)

def get_jump_order_iter(L):
    order = 0
    stack = [L]
    while stack:
        curr = stack.pop()
        if curr and curr.value == -1:
            curr.value = order
            order += 1
            stack.append(curr.next)
            stack.append(curr.jump)

L = [JumpNode() for _ in range(6)]
for i in range(len(L)-1):
    L[i].next = L[i+1]

L[0].jump = L[0]
L[1].jump = L[3]
L[2].jump = L[5]
L[3].jump = L[0]
L[4].jump = L[4]
L[5].jump = L[4]

get_jump_order_iter(L[0])
[print(x.value) for x in L]