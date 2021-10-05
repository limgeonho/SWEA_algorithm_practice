import sys
sys.stdin = open('input.txt')


dx = [1, 0]
dy = [0, 1]

def check(x, y):
    global answer, tmp
    if answer < tmp:
        return
    if x == n-1 and y == n-1:
        answer = tmp
        return
    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            visited[nx][ny] = True
            tmp += board[nx][ny]
            check(nx, ny)
            visited[nx][ny] = False
            tmp -= board[nx][ny]


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    tmp = board[0][0]
    answer = 2147000000
    check(0,0)
    print(f'#{tc} {answer}')