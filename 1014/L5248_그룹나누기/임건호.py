import sys
sys.stdin = open('input.txt')


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    parent = [0] * (n+1)
    for i in range(n+1):
        parent[i] = i

    for i in range(0, m*2, 2):
        union_parent(parent, array[i], array[i+1])

    answer = set()
    for p in parent:
        answer.add(find_parent(parent, p))
    print(f'#{tc} {len(answer)-1}')
