import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    e, n = map(int, input().split())
    array = list(map(int, input().split()))
    cnt = 1
    tree = {}

    for i in range(1, e+2):
        tree[i] = []

    for i in range(0, 2*e, 2):
        tree[array[i]].append(array[i+1])

    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        for nxt in tree[now]:
            cnt += 1
            q.append(nxt)
    print(f'#{tc} {cnt}')

