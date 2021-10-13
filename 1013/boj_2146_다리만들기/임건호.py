from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, check_num):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
                if board[nx][ny] == check_num:
                    visited[nx][ny] = 0
                    q.appendleft((nx, ny))
                elif board[nx][ny] == 0:
                    visited[nx][ny] = visited[now_x][now_y] + 1
                    q.append((nx, ny))
                elif board[nx][ny] != check_num:
                    return visited[now_x][now_y]


def numbering(x, y, num):
    q = deque()
    q.append((x, y))
    board[x][y] = num
    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 1:
                board[nx][ny] = num
                q.append((nx, ny))


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = []

tmp = 2
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            numbering(i, j, tmp)
            tmp += 1


for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            visited = [[-1] * n for _ in range(n)]
            candidate = bfs(i, j, board[i][j])
            if candidate:
                answer.append(candidate)
            else:
                pass

print(min(answer))
