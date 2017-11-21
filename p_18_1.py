import collections

WHITE, BLACK = range(2)
NOT_VISITED, VISITED = range(2)
V = collections.namedtuple('V', ('i', 'j'))

# class Node:
#     def __init__(self, y):
#         self.y = y
#         self.visited = NOT_VISITED
#
#     def __eq__(self, y):
#         return self.y == y
#
#     def __hash__(self):
#         return hash(self.y)

def find_path(maze, start, end):
    graph = {}
    visited = {}
    result = []

    if maze is None:
        return result
    elif start == end:
        return start

    def build_adj_list(i, j):
        col_len = len(maze)
        row_len = len(maze[0])

        if i - 1 >= 0 and maze[i-1][j] == WHITE:
            graph[V(i,j)].append(V(i-1, j))
        if i + 1 < col_len and maze[i+1][j] == WHITE:
            graph[V(i,j)].append(V(i+1, j))
        if j - 1 >= 0 and maze[i][j-1] == WHITE:
            graph[V(i,j)].append(V(i, j-1))
        if j + 1 < row_len and maze[i][j+1] == WHITE:
            graph[V(i,j)].append(V(i, j+1))

    def dfs(v):
        print(v)
        visited[v] = VISITED
        if v == end:
            return v
        for u in graph[v]:
            if visited[u] == NOT_VISITED:
                ret = dfs(u)
                if ret is not None:
                    result.append(ret)
                    return v

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == WHITE:
                visited[V(i, j)] = NOT_VISITED
                graph[V(i, j)] = []
                build_adj_list(i, j)

    dfs(start)
    # [print('{}: {}'.format(x, y)) for x, y in graph.items()]

    return list(reversed(result))

maze = [[WHITE, WHITE, BLACK, WHITE, WHITE],
        [WHITE, BLACK, WHITE, BLACK, WHITE],
        [WHITE, BLACK, WHITE, BLACK, WHITE],
        [WHITE, WHITE, WHITE, BLACK, WHITE],
        [WHITE, WHITE, WHITE, WHITE, WHITE]]
start, end = V(3,0), V(0,3)

A = [1,2,3,4]

print(find_path(maze, start, end))