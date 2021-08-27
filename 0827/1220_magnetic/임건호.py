import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    N = int(input())
    table = []
    cnt = 0
    for _ in range(N):
        table.append(list(map(int, input().split())))
    # 보기 편하려고.. 가로로..
    board = list(zip(*table))

    for i in range(N):
        flag_check = 0
        for j in range(N):
            if board[i][j] == 1:
                flag_check = 1

            elif board[i][j] == 2 and flag_check == 1:
                cnt += 1
                flag_check = 0

    print(f'#{tc} {cnt}')