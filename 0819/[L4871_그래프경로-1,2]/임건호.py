import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    answer = 0
    v, e = map(int, input().split())
    graph = [[0]for _ in range(v+1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)

    s, g = map(int, input().split())

    stack = []
    visited = [False] * (v+1)
    stack.append(s)
    while stack:
        now = stack.pop()
        visited[now] = True
        for i in graph[now]:
            if i == g:
                answer = 1
            else:
                if not visited[i]:
                    visited[i] = True
                    stack.append(i)

    print(f'#{tc} {answer}')