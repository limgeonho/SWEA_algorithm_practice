import sys
sys.stdin = open('input.txt')


def check(x):
    if x > n:
        return
    if x*2 <= n:
        check(x*2)

    answer.append(tree[x])

    if x*2+1 <= n:
        check(x*2+1)

for tc in range(1, 11):
    n = int(input())
    tree = [0] * (n+1)
    for _ in range(n):
        array = list(input().split())
        tree[int(array[0])] = array[1]

    answer = []
    check(1)
    final = ''.join(answer)

    print(f'#{tc} {final}')