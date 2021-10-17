import sys
sys.stdin = open('input.txt')


# def dfs(L, total):
#     global answer
#     if L == n:
#         if answer > total:
#             answer = total
#         return
#
#     if total >= answer:
#         return
#
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = True
#             dfs(L+1, total+array[i][L])
#             visited[i] = False
#
# T = int(input())
#
# for tc in range(1, T+1):
#     n = int(input())
#     array = [list(map(int, input().split())) for _ in range(n)]
#     array = list(zip(*array))
#     visited = [False] * n
#     answer = 2147000000
#     dfs(0, 0)
#     print(f'#{tc} {answer}')

# 여러가지 공장 중에 하나를 골라서 dfs탐색하는 순열문제
def go(L, total):
    global answer
    if L == n:
        if answer > total:
            answer = total
        return
    if total > answer:
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        go(L+1, total + board[L][i])
        visited[i] = False


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    answer = 987654321
    go(0, 0)
    print(f'#{tc} {answer}')