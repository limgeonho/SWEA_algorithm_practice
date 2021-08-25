import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
    s, g = map(int, input().split())
    q = [s]
    visited[s] = 1
    while q:
        now = q.pop(0)
        for next_node in graph[now]:
            if visited[next_node] != 1:
                q.append(next_node)
                visited[next_node] = 1

    if visited[g] == 1:
        answer = 1
    else:
        answer = 0

    print(f'#{tc} {answer}')