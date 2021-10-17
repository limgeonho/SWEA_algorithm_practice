import sys
sys.stdin = open('input.txt')

# 해당 점원을 선택할지 안할지 O, X

def go(L, total, target):
    global answer
    if L == n:
        if target <= total < answer:
            answer = total
        return
    else:
        go(L+1, total + array[L], target)
        go(L + 1, total, target)

T = int(input())

for tc in range(1, T+1):
    n, b = map(int, input().split())
    array = list(map(int, input().split()))
    answer = 987654321
    go(0, 0, b)

    print(f'#{tc} {answer - b}')