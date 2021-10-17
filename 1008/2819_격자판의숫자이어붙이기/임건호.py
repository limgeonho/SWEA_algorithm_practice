import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(x, y, arr):
    if len(arr) == 7:
        answer.add(arr)
        return
    else:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<4 and 0<=ny<4:
                go(nx, ny, arr + array[nx][ny])

T = int(input())

for tc in range(1, T+1):
    array = [list(map(str, input().split())) for _ in range(4)]
    answer = set()
    for i in range(4):
        for j in range(4):
            go(i, j, '')
    print(f'#{tc} {len(answer)}')