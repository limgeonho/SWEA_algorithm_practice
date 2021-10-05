import sys
sys.stdin = open('input.txt')


def check(p):
    for i in range(len(p)):
        if p[i] == 3:
            return True

    for j in range(len(p)-2):
        if p[j] and p[j+1] and p[j+2]:
            return True

    return False


T = int(input())
for tc in range(1, T+1):
    array = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    answer = 0
    for i in range(len(array)):
        if i % 2 == 0:
            p1[array[i]] += 1
            if check(p1):
                answer = 1
                break
        else:
            p2[array[i]] += 1
            if check(p2):
                answer = 2
                break

    print(f'#{tc} {answer}')

