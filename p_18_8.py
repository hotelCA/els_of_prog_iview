# from functools import total_ordering

# @total_ordering
class Team:
    def __init__(self, heights):
        self.heights = [h for h in heights]

    def __eq__(self, other):
        return all(x == y for x, y in zip(self.heights, other.heights))

    def __gt__(self, other):
        return all(x > y for x, y in zip(self.heights, other.heights))

    def __lt__(self, other):
        return all(x < y for x, y in zip(self.heights, other.heights))

def find_max_teams_photo(teams):
    result = 1

    def dfs(u, count):
        nonlocal result
        if G[u] == [] and count > result:
            result = count
        else:
            for v in G[u]:
                dfs(v, count+1)

    sorted_teams = [Team(sorted(x.heights)) for x in teams]
    num_teams = len(sorted_teams)
    G = {i: [] for i in range(num_teams)}

    for i in range(num_teams):
        for j in range(i+1, num_teams):
            if sorted_teams[i] > sorted_teams[j]:
                G[i].append(j)
            elif sorted_teams[i] < sorted_teams[j]:
                G[j].append(i)
    print(G)
    for u in G:
        dfs(u, 1)
    return result

A = [1,2,3,4,5]
B = [2,3,4,5,6]
C = [3,4,5,6,7]
D = [4,5,6,7,8]
E = [3,4,5,6,7]
F = [4,5,6,7,8]
G = [1,2,3,4,5]
H = [2,3,4,5,6]

teams = [Team(D),Team(C),Team(A),Team(B),Team(E),Team(F),Team(G),Team(H)]
print(find_max_teams_photo(teams))