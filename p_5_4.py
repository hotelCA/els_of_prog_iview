def winnable(board):
    next_step = len(board) - 1
    for i in reversed(range(len(board)-1)):
        if i + board[i] >= next_step:
            print('Next step: {step}'.format(step=i))
            if i == 0:
                return True
            next_step = i

    return False

def winnable_2(board):

    if len(board) == 1 or len(board) == 0:
        return 0

    max_distance = [min(board[0], len(board)-1)]
    for i in range(1, len(board)):
        if i > max_distance[i-1]:
            return False
        max_distance.append(min(max(max_distance[i-1], i+board[i]), len(board)-1))
    print(max_distance)

    steps = 1
    for i in reversed(range(len(max_distance))):
        if i == 0:
            return steps
        if max_distance[i] != max_distance[i-1]:
            steps += 1

# print(winnable([3,3,1,1,2,0,1]))
print(winnable_2([3,3,1,1,2,0,1]))
print(winnable_2([7,0]))
print(winnable_2([2]))
print(winnable_2([1,0,2]))
print(winnable_2([0]))
print(winnable_2([1,1,1,1,1,1,1]))

