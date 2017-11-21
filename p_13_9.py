def order_team_photo(team_A, team_B):
    if len(team_A) != len(team_B) or len(team_A) == 0:
        return

    team_A.sort(), team_B.sort()
    sign = team_B[0] - team_A[0]
    if sign == 0:
        return -1

    for i in range(1, len(team_A)):
        diff = team_B[i] - team_A[i]
        if sign * diff <= 0:
            return -1

    return [team_B, team_A] if sign > 0 else [team_A, team_B]

B = [3,4,5,6,7,9]
A = [4,5,6,7,8,90]
print(order_team_photo(A, B))