import sys
sys.stdin = open('input.txt')

from heapq import heapify

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    array = list(map(int, input().split()))

    nodes = []
    for element in array:
        nodes.append(element)

        heapify(nodes)

    answer = 0
    while n > 0:
        n //= 2
        if n == 0:
            break
        answer += nodes[n-1]

    print(f'#{tc} {answer}')