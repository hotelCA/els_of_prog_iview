class Vertex:
    white, grey, black = range(3)

    def __init__(self, name):
        self.color = Vertex.white
        self.name = name
        self.edges = []

def detect_cycle(G):
    def dfs(u):
        print(u.name)
        u.color = Vertex.grey
        ret_val = False
        for v in u.edges:
            if v.color == Vertex.grey:
                return True
            elif v.color == Vertex.white:
                ret_val = dfs(v)

            if ret_val == True:
                return True
        u.color = Vertex.black
        return False
    return any(v.color == Vertex.white and dfs(v) for v in G)

G = [Vertex(chr(x)) for x in range(ord('A'), ord('H'))]
G[0].edges.append(G[1])
G[1].edges.append(G[2])
G[2].edges.append(G[3])
G[2].edges.append(G[4])
G[4].edges.append(G[5])
G[4].edges.append(G[6])
G[5].edges.append(G[3])

# G[5].edges.append(G[1])

print(detect_cycle(G))
