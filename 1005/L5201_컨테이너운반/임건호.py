import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    container.sort(reverse=True)
    truck.sort(reverse=True)

    answer = 0
    for i in range(len(truck)):
        for j in range(len(container)):
            if truck[i] >= container[j]:
                answer += container[j]
                container.remove(container[j])
                break
            else:
                continue
    print(f'#{tc} {answer}')