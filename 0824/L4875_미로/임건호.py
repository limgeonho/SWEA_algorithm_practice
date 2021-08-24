import sys
sys.stdin = open('input.txt')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(s_i, s_j):
    global answer

    if maze[s_i][s_j] == '3':
        answer = 1
        return answer

    visited.append((s_i, s_j))
    for t in range(4):
        next_i = s_i + dx[t]
        next_j = s_j + dy[t]
        if 0 <= next_i < n and 0 <= next_j < n and (next_i, next_j) not in visited and (maze[next_i][next_j] == '0' or maze[next_i][next_j] == '3'):
            DFS(next_i, next_j)


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    maze = []
    visited = []

    answer = 0
    for _ in range(n):
        maze.append(input())
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                s_i = i
                s_j = j

    DFS(s_i, s_j)

    print(f'#{tc} {answer}')