import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(start, graph, x):
    q = []
    distance = [sys.maxsize] * (n+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

T = int(input())

for tc in range(1, T+1):
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    answer = []
    for _ in range(m):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))

    go = dijkstra(x, graph, x)
    for i in range(1, n+1):
        if i == x:
            continue
        else:
            tmp = dijkstra(i, graph, x)
            answer.append(tmp[x] + go[i])

    print(f'#{tc} {max(answer)}')