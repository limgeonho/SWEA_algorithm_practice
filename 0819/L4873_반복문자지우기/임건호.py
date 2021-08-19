import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    s = input()
    stack = []

    for i in range(len(s)//2):
        for j in range(len(s)-1):
            if s[j] == s[j+1]:
                tmp = s[:j] + s[j+2:]
                s = tmp
                break
    print(f'#{tc} {len(s)}')
