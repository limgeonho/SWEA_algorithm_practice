import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    array = []
    for _ in range(n):
        array.append(input())

    q = deque()
    check = [[-1] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if array[i][j] == 'W':
                q.append((i, j))
                check[i][j] = 0
    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<m and array[nx][ny] == 'L' and check[nx][ny] == -1:
                check[nx][ny] = check[now_x][now_y] + 1
                q.append((nx, ny))

    answer = 0
    for row in check:
        answer += sum(row)

    print(f'#{tc} {answer}')
