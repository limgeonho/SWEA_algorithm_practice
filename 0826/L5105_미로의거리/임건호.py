import sys
from collections import deque
sys.stdin = open('input.txt')

moves = ((-1, 0), (0, 1), (1, 0), (0, -1))


def bfs(start_y, start_x, maze, dist):
    q = deque()
    q.append((start_y, start_x))
    maze[start_y][start_x] = 1
    while q:
        y, x = q.popleft()
        for dy, dx in moves:
            ny = y + dy
            nx = x + dx
            if 0 <= ny <n and 0 <= nx <n and (maze[ny][nx] == 0 or maze[ny][nx] == 3):
                if maze[ny][nx] == 3:
                    return dist[y][x]
                else:
                    maze[ny][nx] = 1
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))


def find_start(maze):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                y, x = i, j
                return y, x
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    maze = []

    for _ in range(n):
        maze.append(list(map(int, input())))
    s_y, s_x = find_start(maze)

    dist = [[0] * n for _ in range(n)]

    answer = bfs(s_y, s_x , maze, dist)

    if answer:
        print(f'#{tc} {answer}')
    else:
        print(f'#{tc} {0}')