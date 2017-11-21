import copy

def n_non_attacking_queens(n):

    def find_next_position(positions, col):

        for i in range(0, n):
            if positions[i][col] == 0:
                new_positions = copy.deepcopy(positions)
                new_positions[i][col] = 2
                if col == n - 1:
                    result.append(new_positions)
                else:
                    update_positions(new_positions, col+1, i)
                    find_next_position(new_positions, col+1)

    def update_positions(positions, col, row):
        for i in range(col, n):
            positions[row][i] = 1
        lower, upper = row - 1, row + 1
        while (lower >= 0 or upper < n) and col < n:
            # print('{}, {}, {}'.format(lower, upper, col))
            if lower >= 0:
                positions[lower][col] = 1
                lower -= 1
            if upper < n:
                positions[upper][col] = 1
                upper += 1
            col += 1

    result = []
    board = [[0 for i in range(n)] for j in range(n)]
    find_next_position(board, 0)

    return result

result = n_non_attacking_queens(4)
# print([[print(y) for y in x] for x in result])
# print(result)
print(len(result))