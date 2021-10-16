import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0,-1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<n:
                power = 0
                if array[nx][ny] > array[now_x][now_y]:
                    power = array[nx][ny] - array[now_x][now_y]
                if visited[nx][ny] > visited[now_x][now_y] + power + 1:
                    visited[nx][ny] = visited[now_x][now_y] + power + 1
                    q.append((nx, ny))

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    visited = [[987654321] * n for _ in range(n)]
    bfs(0, 0)
    print(f'#{tc} {visited[-1][-1]}')