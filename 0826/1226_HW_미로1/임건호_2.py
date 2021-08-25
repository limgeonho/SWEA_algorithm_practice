import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(i, j):
    global answer
    if maze[i][j] == 3:
        answer = 1
        return
    else:
        for d in range(4):
            ni = i + dx[d]
            nj = j + dy[d]
            if visited[ni][nj] == 0 and (maze[ni][nj] == 0 or maze[ni][nj] == 3):
                visited[ni][nj] = 1
                dfs(ni, nj)
                visited[ni][nj] = 0


def find_start(maze):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start_i, start_j = i, j
                return start_i, start_j


for tc in range(1, 11):
    T = int(input())
    maze = []
    answer = 0
    visited = [[0]*16 for _ in range(16)]
    for _ in range(16):
        maze.append(list(map(int, input())))

    s_i, s_j = find_start(maze)
    dfs(s_i, s_j)
    print(f'#{tc} {answer}')
