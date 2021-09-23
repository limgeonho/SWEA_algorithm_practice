import sys
sys.stdin = open('input.txt')

def check(x):
    global cnt
    if x <= n:
        check(2*x)
        tree[x] = cnt
        cnt += 1
        check(2*x+1)

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    tree = [0] * (n+1)

    cnt = 1
    check(1)
    print(f'#{tc} {tree[1]} {tree[n//2]}')