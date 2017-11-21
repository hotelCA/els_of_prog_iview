import collections

V = collections.namedtuple('V', ('i', 'j'))
WHITE, BLACK = range(2)

def flip_color(maze, U):
    i, j = U[0], U[1]
    target_color = maze[i][j]
    maze[i][j] = 1^target_color
    col_len = len(maze)
    row_len = len(maze[i])

    for v in (-1,0),(1,0),(0,-1),(0,1):
        next_x, next_y = i + v[0], j + v[1]
        if (0 <= next_x < col_len) and (0 <= next_y < row_len) and (maze[next_x][next_y] == target_color):
            flip_color(maze, V(next_x, next_y))

maze = [[WHITE, BLACK, WHITE, WHITE],
        [BLACK, WHITE, BLACK, WHITE],
        [WHITE, WHITE, BLACK, WHITE],
        [BLACK, BLACK, WHITE, WHITE]]
start = V(1,1)

flip_color(maze, start)
[print(row) for row in maze]