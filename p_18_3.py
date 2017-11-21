import collections
WHITE, BLACK, GREY = range(3)

def invert_inner_cells(maze):
    n, m = len(maze), len(maze[0])

    def filter_white_cells(x):
        return maze[x[0]][x[1]] == WHITE

    _lambda = filter_white_cells
    Q = collections.deque(list(filter(_lambda,
                            [(i, j) for k in range(n) for i, j in ((k, 0), (k, m-1))] +
                            [(i, j) for k in range(m) for i, j in ((0, k),(n-1, k))])))

    while Q:
        i, j = Q.popleft()
        maze[i][j] = GREY
        for x, y in (i-1, j),(i+1, j),(i, j-1),(i, j+1):
            if 0 <= x < n and 0 <= y < m and maze[x][y] == WHITE:
                Q.append((x, y))

    maze[:] = [[BLACK if c != GREY else WHITE for c in row] for row in maze]

maze = [[BLACK, BLACK, WHITE, BLACK],
        [BLACK, BLACK, WHITE, BLACK],
        [BLACK, WHITE, BLACK, WHITE],
        [BLACK, BLACK, BLACK, BLACK]]

invert_inner_cells(maze)
[print(u) for u in maze]
