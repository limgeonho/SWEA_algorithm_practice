import sys
from itertools import permutations
sys.stdin = open('input.txt')


def check(L):
    global sum_nums, min_num
    if sum_nums > min_num:
        return
    if L == n:
        min_num = min(sum_nums, min_num)
        return
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                sum_nums += board[L][i]
                check(L+1)
                visited[i] = False
                sum_nums -= board[L][i]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    board = []
    visited = [False] * n
    min_num = 1000
    sum_nums = 0
    for _ in range(n):
        board.append(list(map(int, input().split())))

    check(0)
    print(f'#{tc} {min_num}')