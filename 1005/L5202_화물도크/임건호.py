import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    time = []
    for _ in range(n):
        s, e = map(int, input().split())
        time.append((s, e))


    changed = sorted(time, key = lambda x:x[1])
    candidate = [changed[0]]

    for i in range(1, len(changed)):
        if candidate[-1][1] <= changed[i][0]:
            candidate.append(changed[i])

    print(f'#{tc} {len(candidate)}')