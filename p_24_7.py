def attacking_rooks(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 0:
                M[0][j] = 0
                M[i][0] = 0

    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[0][j] == 0 or M[i][0] == 0:
                if i != 0 and j != 0:
                    M[i][j] = 0
    print()
    for L in M:
        print(L)

M = [[1] * 8 for _ in range(10)]
M[0][5] = 0
M[2][7] = 0
M[4][1] = 0
M[9][3] = 0
M[5][5] = 0
M[7][6] = 0
attacking_rooks(M)
    