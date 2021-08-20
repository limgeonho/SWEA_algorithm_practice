import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    rooms = [0] * 201

    n = int(input())

    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        a = (a + 1) // 2
        b = (b + 1) // 2
        for i in range(a, b+1):
            rooms[i] += 1

    print(f'#{tc} {max(rooms)}')

