import sys
sys.stdin = open('input.txt')


def dfs(L, total):
    global answer
    if L == n:
        if answer > total:
            answer = total
        return

    if total >= answer:
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(L+1, total+array[i][L])
            visited[i] = False

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    array = list(zip(*array))
    visited = [False] * n
    answer = 2147000000
    dfs(0, 0)
    print(f'#{tc} {answer}')
