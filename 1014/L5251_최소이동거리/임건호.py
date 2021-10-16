import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

T = int(input())

for tc in range(1, T+1):
    n, e = map(int, input().split())

    distance = [sys.maxsize] * (n+1)

    graph = [[] for _ in range(n+1)]

    for _ in range(e):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    dijkstra(0)
    print(f'#{tc} {distance[n]}')
