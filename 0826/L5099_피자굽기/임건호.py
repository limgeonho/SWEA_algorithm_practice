import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    pizza_with_idx = []
    fire = []

    for idx, cheese in enumerate(pizza):
        pizza_with_idx.append((idx+1, cheese))

    for _ in range(N):
        fire.append(pizza_with_idx.pop(0))

    while True:
        if len(pizza_with_idx) == 0 and len(fire) == 1:
            answer = fire[0][0]
            break

        tmp = fire.pop(0)
        tmp_pizza = (tmp[0], tmp[1] // 2)

        if tmp_pizza[1] == 0:
            if len(pizza_with_idx) == 0:
                continue
            else:
                tmp_pizza = pizza_with_idx.pop(0)
        fire.append(tmp_pizza)

    print(f'#{tc} {answer}')