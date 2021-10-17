import sys
sys.stdin = open('input.txt')

# T = int(input())
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def find_room(x, y, cnt):
#     global ans, ans_num
#     if cnt > ans:
#         ans = cnt
#         ans_num = room_list[a][b]
#     if cnt == ans and ans_num > room_list[a][b]:
#         ans = cnt
#         ans_num = room_list[a][b]
#     for i in range(4):
#         new_x = x + dx[i]
#         new_y = y + dy[i]
#         if new_x < N and new_y < N and room_list[new_x][new_y] == room_list[x][y] + 1:
#             find_room(new_x, new_y, cnt + 1)
#
#
# for tc in range(1, T + 1):
#     N = int(input())
#     room_list = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0
#     ans_num = 100000
#     for a in range(N):
#         for b in range(N):
#             find_room(a, b, 1)
#     print('#{} {} {}'.format(tc, ans_num, ans))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(x, y, cnt):
    global answer_num, answer
    if cnt > answer:
        answer = cnt
        answer_num = array[i][j]

    if answer == cnt and answer_num > array[i][j]:
        answer = cnt
        answer_num = array[i][j]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<n and array[nx][ny] == array[x][y] + 1:
            go(nx, ny, cnt+1)

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    answer_num = 987654321
    for i in range(n):
        for j in range(n):
            go(i, j, 1)

    print(f'#{tc} {answer_num} {answer}')


