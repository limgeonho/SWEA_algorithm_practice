import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 1. 현재 위치를 들고 다니지 않을 때
# r, c는 좌표, road 는 지금까지 조성된 등산로의 길이, skill 공사 유무
def work(r, c, road, skill):
    global answer
    if road > answer:
        answer = road

    visited[r][c] = 1
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            # a. 현위치보다 낮은 곳으로 이동할 때
            if mountatin[r][c] > mountatin[nx][ny]:
                work(nx, ny, road+1, skill)
            # b. 현위치보다 높거나 같은곳으로 이동할 때
            elif skill and mountatin[r][c] > mountatin[nx][ny] - k:
                tmp = mountatin[nx][ny]
                mountatin[nx][ny] = mountatin[r][c] - 1
                work(nx, ny, road+1, 0) # skill 사용
                mountatin[nx][ny] = tmp # 원상복구
    visited[r][c] = 0

# 2. 현재위치를 들고다닌다면?
def work2(r, c, h, road, skill):
    global answer
    if road > answer:
        answer = road
    visited[r][c] = 1
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n and visited[nx][ny]:
            continue
        if h > mountatin[nx][ny]:
            work2(nx, ny, mountatin[nx][ny], road+1, skill)
        elif skill and h > mountatin[nx][ny] - k:
            work2(nx, ny, mountatin[r][c]-1, road+1, 0)

    visited[r][c] = 0

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())

    mountatin = [list(map(int, input().split())) for _ in range(n)]
    max_h = 0

    # 최고 높은 봉우리 찾기
    for i in range(n):
        for j in range(n):
            if max_h < mountatin[i][j]:
                max_h = mountatin[i][j]

    # 산의 정보를 입력받으면서 동시에 최고 높은 봉우리 찾는 방법
    # mountatin = []
    # max_h = 0
    # for i in range(n):
    #     tmp = list(map(int, input().split()))
    #     # 한 줄 씩 입력을 받고 내부에서 가장 큰값을 찾자
    #     for j in tmp:
    #         if max_h < j:
    #             max_h = j
    #     mountatin.append(tmp)

    visited = [[0] * n for _ in range(n)]
    answer = 0

    for i in range(n):
        for j in range(n):
            if mountatin[i][j] == max_h:
                work(i, j, 1, 1)
                # work2(i, j, max_h, 1, 1)
    print(f'#{tc} {answer}')