import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global answer, tmp
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            tmp += array[nx][ny]

            visited[nx][ny] = True
            dfs(nx,ny)
            visited[nx][ny] = False
            if nx == n - 1 and ny == n - 1:
                if answer < tmp:
                    answer = tmp
                return

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    visited = [[False] * n for _ in range(n)]
    array = [list(map(int, input())) for _ in range(n)]

    answer = 987654321
    tmp = array[0][0]
    visited[0][0] = True
    dfs(0,0)
    print(answer)