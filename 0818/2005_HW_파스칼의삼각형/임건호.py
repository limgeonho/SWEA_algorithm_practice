import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    tri = list([1] for _ in range(n))
    for i in range(n):
        for j in range(i):
            tri[i].append(1)

    for i in range(2, n):
        for j in range(1, i):
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]

    print(f'#{tc}')
    for i in range(n):
        print(*tri[i])