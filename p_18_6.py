class Vertex:
    def __init__(self):
        self.y = -1
        self.edges = []

def group_connectors(pcb):
    def dfs(u, time):
        u.y = time
        for v in u.edges:
            print('u: {}, v: {}'.format(u.y, v.y))
            if v.y == -1:
                if not dfs(v, time + 1):
                    return False
            elif (v.y % 2) == (u.y % 2):
                return False

        return True

    return all(dfs(u, 0) for u in pcb if u.y == -1)

pcb = [Vertex() for _ in range(7)]
pcb[0].edges.append(pcb[1])
pcb[1].edges.append(pcb[0])
pcb[1].edges.append(pcb[2])
pcb[1].edges.append(pcb[4])
pcb[2].edges.append(pcb[1])
pcb[2].edges.append(pcb[3])
pcb[3].edges.append(pcb[2])
pcb[3].edges.append(pcb[4])
pcb[4].edges.append(pcb[1])
pcb[4].edges.append(pcb[3])
pcb[4].edges.append(pcb[5])
pcb[4].edges.append(pcb[6])
pcb[5].edges.append(pcb[4])
pcb[5].edges.append(pcb[6])
pcb[6].edges.append(pcb[5])
pcb[6].edges.append(pcb[4])
# [print(len(x.edges)) for x in pcb]

print(group_connectors(pcb))