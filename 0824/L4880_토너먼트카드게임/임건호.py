import sys
sys.stdin = open('input.txt')

def game(a, b):
    if (a == 1 and b == 3) or (a == 1 and b == 1):
        return 1
    elif (a == 2 and b == 1) or (a == 2 and b == 2):
        return 2
    elif (a == 3 and b == 2) or (a == 3 and b == 3):
        return 3
    return 0


def match(cards):
    n = len(cards)
    if n < 2:
        return cards[0]

    if n % 2:
        left = cards[:n//2+1]
        right = cards[n//2+1:]
    else:
        left = cards[:n//2]
        right = cards[n//2:]
    a = match(left)
    b = match(right)

    if game(a[0], b[0]):
        return a
    else:
        return b


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    cards = list(map(int, input().split()))
    cards = [(n, i+1) for i, n in enumerate(cards)]
    print(f'#{tc} {match(cards)[1]}')