import sys

class Vertex:
    def __init__(self, y, weight=0):
        self.y = y
        self.weight = weight

    def __hash__(self):
        return hash(self.y)

def shortest_fewest_edges(G, s, t):
    finished = set()
    dist = {key: sys.maxsize for key in G}
    dist[s] = 0
    parent = {}
    current = (s, 0)

    while current[0] != t:
        finished.add(current[0])
        for v in G[current[0]]:
            if v.y not in finished:
                if dist[current[0]] + v.weight < dist[v.y]:
                    dist[v.y] = dist[current[0]] + v.weight
                    parent[v.y] = (current[0], current[1] + 1)
                elif dist[current[0]] + v.weight == dist[v.y]:
                    if parent[v.y][1] > current[1] + 1:
                        parent[v.y] = (current[0], current[1] + 1)

        shortest = sys.maxsize
        for key, value in dist.items():
            if key not in finished and value < shortest:
                shortest = value
                current = (key, parent[key][1] + 1)
        if shortest == sys.maxsize:
            break

    result = []
    current = t
    while current != s:
        result.append(current)
        current = parent[current][0]

    return result

G = {chr(x): [] for x in range(ord('A'), ord('H'))}
G['A'].append(Vertex('B', 3)), G['A'].append(Vertex('C', 3)), G['A'].append(Vertex('D', 2))
G['B'].append(Vertex('A', 2)), G['B'].append(Vertex('C', 5)), G['B'].append(Vertex('D', 4)), G['B'].append(Vertex('F', 3)), G['B'].append(Vertex('G', 1))
G['C'].append(Vertex('A', 3)), G['C'].append(Vertex('B', 5)), G['C'].append(Vertex('G', 5))
G['D'].append(Vertex('A', 2)), G['D'].append(Vertex('B', 4)), G['D'].append(Vertex('E', 7)), G['D'].append(Vertex('F', 4))
G['E'].append(Vertex('D', 7)), G['E'].append(Vertex('F', 6))
G['F'].append(Vertex('B', 4)), G['F'].append(Vertex('D', 5)), G['F'].append(Vertex('E', 6)), G['F'].append(Vertex('G', 3))
G['G'].append(Vertex('B', 1)), G['G'].append(Vertex('C', 5)), G['G'].append(Vertex('F', 3))

print(shortest_fewest_edges(G, 'A', 'F'))