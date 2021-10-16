import sys
import heapq
sys.stdin = open('input.txt')


# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# T = int(input())
#
# for tc in range(1, T+1):
#     v, e = map(int, input().split())
#
#     edges = []
#     for _ in range(e):
#         a, b, cost = map(int, input().split())
#         edges.append((cost, a, b))
#
#     edges.sort()
#
#     parent = [0] * (v+1)
#     for i in range(v+1):
#         parent[i] = i
#
#     result = 0
#     for edge in edges:
#         cost, a, b = edge
#         if find_parent(parent, a) != find_parent(parent, b):
#             union_parent(parent, a, b)
#             result += cost
#
#     print(f'#{tc} {result}')


def prim():
    q = []
    heapq.heappush(q, (0, 0))
    answer = 0
    while q:
        w, v = heapq.heappop(q)
        if not visited[v]:
            answer += w
            visited[v] = True

            for idx, weight in graph[v]:
                if not visited[idx]:
                    heapq.heappush(q, (weight, idx))

    return answer


T = int(input())

for tc in range(1, T+1):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]
    visited = [False] * (v + 1)

    for _ in range(e):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    tmp = prim()

    print(f'#{tc} {tmp}')