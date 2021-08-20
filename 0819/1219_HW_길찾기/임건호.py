import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    t, n = map(int, input().split())
    graph = [[]for _ in range(100)]
    link = list(map(int, input().split()))

    for i in range(0, 2*n, 2):
        graph[link[i]].append(link[i+1])

    stack = []
    stack.append(0)
    answer = 0
    visited = [False] * 100
    while stack:
        now = stack.pop()
        visited[now] = True

        for i in graph[now]:
            if i == 99:

                answer = 1
                break
            else:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True

    print(f'#{t} {answer}')
