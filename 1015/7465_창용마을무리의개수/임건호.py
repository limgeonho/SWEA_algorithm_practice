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
    parent = [i for i in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    answer = set()

    # for i in range(1, n+1):
    #     answer.add(find_parent(parent, i))
    ans = 0
    for i in range(1, n+1):
        if i == parent[i]:
            ans += 1

    print(f'#{tc} {ans}')