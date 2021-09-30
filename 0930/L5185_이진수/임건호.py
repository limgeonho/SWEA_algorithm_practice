import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, number = input().split()
    answer = ''
    for i in range(int(n)):
        answer += bin(int(number[i], 16))[2:].rjust(4, '0')

    print(f'#{tc} {answer}')