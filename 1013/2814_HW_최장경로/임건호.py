# import sys
# sys.stdin = open('input.txt')


def dfs(start, answer):
    global final

    if answer > final:
        final = answer

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, answer+1)
            visited[i] = False


T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    final = 0
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n+1):
        visited[i] = True
        dfs(i, 1)
        visited[i] = False

    print(graph)
    print(f'#{tc} {final}')
