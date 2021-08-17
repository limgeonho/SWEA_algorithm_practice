import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    answer = []

    for s in str1:
        answer.append(str2.count(s))

    print(f'#{tc} {max(answer)}')
