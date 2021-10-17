import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(start):
    q = deque()
    q.append(start)

    check[start] = 0

    while q:
        now = q.popleft()
        for nxt in (now+1, now-1, now*2, now-10):
            if 0<nxt<=1000000 and check[nxt] == -1:
                q.append(nxt)
                check[nxt] = check[now] + 1
                if nxt == m:
                    return
T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    check = [-1] * 1000001
    bfs(n)
    print(f'#{tc} {check[m]}')