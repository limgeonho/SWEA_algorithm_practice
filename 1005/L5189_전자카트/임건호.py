import sys
sys.stdin = open('input.txt')

from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split()))for _ in range(n)]

    path = range(2, n+1)
    candidate = []
    for i in permutations(path, n-1):
        candidate.append([1] + list(i) + [1])
    answer = 2147000000
    for can in candidate:
        tmp = 0
        for i in range(len(can)-1):
            tmp += board[can[i]-1][can[i+1]-1]
        if answer > tmp:
            answer = tmp

    print(f'#{tc} {answer}')
