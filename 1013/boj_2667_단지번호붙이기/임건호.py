# 단지번호 붙이기

from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = '0'
    number = 0
    while q:
        now_x, now_y = q.popleft()
        number += 1
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == '1':
                board[nx][ny] = '0'
                q.append((nx, ny))
    return number


n = int(input())

board = [list(input()) for _ in range(n)]

cnt = 0
answer = []
for i in range(n):
    for j in range(n):
        if board[i][j] == '1':
            tmp = bfs(i, j)
            answer.append(tmp)
            cnt += 1

answer.sort()
print(cnt)
for ans in answer:
    print(ans)