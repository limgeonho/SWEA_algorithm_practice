import sys
sys.stdin = open('input.txt')

# T = int(input())
#
# for tc in range(1, T+1):
#     n = int(input())
#     money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
#     cnt = [0] * 8
#     while True:
#         if n == 0:
#             break
#         for i in range(8):
#             if n >= money[i]:
#                 cnt[i] = n // money[i]
#                 n = n % money[i]
#             else:
#                 continue
#     print(f'#{tc}')
#     print(*cnt)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []

    for i in range(len(money)):
        result.append(N // money[i])
        N %= money[i]
    print('#{}'.format(tc))
    print(*result)