import sys
sys.stdin = open('input.txt')

def rotate_matrix_by_90_degree_1(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]

    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res

for tc in range(1, 11):
    N = int(input())
    table = []
    cnt = 0
    for _ in range(N):
        table.append(list(map(int, input().split())))
    # 보기 편하려고.. 가로로..
    board = rotate_matrix_by_90_degree_1(table)

    for i in range(N):
        flag_1 = 0
        for j in range(N):
            if board[i][j] == 1 and flag_1 == 0:
                board[i][j] = 0
            elif board[i][j] == 2:
                flag_1 = 1

    for i in range(N):
        flag_2 = 0
        for j in range(N):
            if board[i][-j - 1] == 2 and flag_2 == 0:
                board[i][-j - 1] = 0
            elif board[i][-j - 1] == 1:
                flag_2 = 1

    for i in range(N):
        flag_check = 0
        for j in range(N):
            if board[i][j] == 2 and flag_check == 0:
                cnt += 1
                flag_check = 1
            elif board[i][j] == 1:
                flag_check = 0

    print(f'#{tc} {cnt}')