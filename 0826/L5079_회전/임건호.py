import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    answer = 0

    for _ in range(m):
        array.append(array.pop(0))

    print(f'#{tc} {array[0]}')