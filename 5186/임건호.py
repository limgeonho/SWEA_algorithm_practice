import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = float(input())
    answer = ''

    for cnt in range(12):
        n *= 2
        answer += str(int(n))
        n -= int(n)
        if n == 0:
            break
    else:
        answer = 'overflow'
    print(f'#{tc} {answer}')


