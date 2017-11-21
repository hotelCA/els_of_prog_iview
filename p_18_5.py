import collections
import copy

class Vertex:
    white, black = range(2)
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.color = Vertex.white

    # def __copy__(self):
    #     new_copy = Vertex(self.id)
    #     new_copy.edges = copy.deepcopy(self.edges)

def copy_graph(G, u):
    copied_graph = []

    bfs_queue = collections.deque([u])

    while bfs_queue:
        u = bfs_queue.popleft()
        copied_graph.append(Vertex(u.id))
        u.color = Vertex.black
        for v in u.edges:
            copied_graph[-1].edges.append(Vertex(v.id))
            if v.color == Vertex.white:
                bfs_queue.append(v)

    return copied_graph

G = [Vertex(x) for x in range(8)]
G[0].edges.append(G[1])
G[0].edges.append(G[2])
G[2].edges.append(G[1])
G[2].edges.append(G[3])
G[3].edges.append(G[4])
G[3].edges.append(G[6])
G[4].edges.append(G[5])
G[5].edges.append(G[3])
G[6].edges.append(G[7])

output = copy_graph(G, G[6])
for u in output:
    print('{}: '.format(u.id), end='')
    for v in u.edges:
        print('{}, '.format(v.id), end='')
    print()