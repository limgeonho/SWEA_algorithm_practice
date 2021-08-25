import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    dist = [0 for _ in range(v+1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    s, g = map(int, input().split())
    q = deque()
    q.append(s)
    dist[s] = 0
    answer = 0
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if dist[next_node] == 0:
                dist[next_node] = dist[now] + 1
                q.append(next_node)
    if dist[g] != 0:
        print(f'#{tc} {dist[g]}')
    else:
        print(f'#{tc} {0}')
