import sys
sys.stdin = open('input-a.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    array = list(map(int, input().split()))
    answer = 0
    price = array[-1]

    # 거꾸로
    for i in range(n-2, -1, -1):
        if price > array[i]:
            answer += (price - array[i])
        else:
            price = array[i]

    print(f'#{tc} {answer}')