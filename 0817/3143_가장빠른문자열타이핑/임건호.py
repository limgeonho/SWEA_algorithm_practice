import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    a, b = input().split()
    cnt = 0
    cnt = a.count(b)
    answer = len(a) - (cnt * len(b)) + cnt

    print(f'#{tc} {answer}')