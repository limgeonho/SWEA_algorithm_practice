import sys
sys.stdin = open('input.txt')

from collections import deque

tunnel = {
    0: (),
    1: ((1, 0), (0, 1), (-1, 0), (0, -1)),
    2: ((1, 0), (-1, 0)),
    3: ((0, 1), (0, -1)),
    4: ((-1, 0), (0, 1)),
    5: ((1, 0), (0, 1)),
    6: ((1, 0), (0, -1)),
    7: ((-1, 0), (0, -1))
}


T = int(input())
for tc in range(1, T+1):
    n, m, r, c, l = map(int, input().split())
    array = []
    for _ in range(n):
        array.append(list(map(int, input().split())))

    q = deque()
    cnt = 1
    check = [[0] * m for _ in range(n)]

    q.append((r,c))
    check[r][c] = 1
    while q:
        now_x, now_y = q.popleft()
        for tnx, tny in tunnel[array[now_x][now_y]]:

            nx = now_x + tnx
            ny = now_y + tny
            if not 0<=nx<n or not 0<=ny<m:
                continue
            if (-tnx, -tny) in tunnel[array[nx][ny]] and not check[nx][ny]:
                check[nx][ny] = check[now_x][now_y] + 1
                q.append((nx, ny))
                if check[nx][ny] <= l:
                    cnt += 1

    print(f'#{tc} {cnt}')