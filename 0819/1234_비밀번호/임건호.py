import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n, password = map(str, input().split())
    stack = []

    for i in range(len(password) // 2):
        for j in range(len(password) - 1):
            if password[j] == password[j + 1]:
                tmp = password[:j] + password[j + 2:]
                password = tmp
                break

    print(f'#{tc} {password}')