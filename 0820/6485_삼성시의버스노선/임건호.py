import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    route = []
    stop = [0] * 5001
    answer = []

    for _ in range(N):
        s, e = map(int, input().split())
        for j in range(s, e+1):
            stop[j] += 1

    P = int(input())

    for _ in range(P):
        answer.append(stop[int(input())])


    print(f'#{tc}', end=' ')
    print(*answer)