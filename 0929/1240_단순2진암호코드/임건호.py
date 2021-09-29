import sys
sys.stdin = open('input.txt')

check = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4', '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    array = []
    tmp = ''
    for _ in range(n):
        code = input()
        rstrip_code = code.rstrip('0')
        length = len(rstrip_code)
        if length:
            tmp = rstrip_code[(length-56):]
            continue
    a = 0
    decode = ''
    while True:
        if a == 56:
            break
        decode += check[tmp[a:a+7]]
        a += 7
    tmp_1 = 0
    tmp_2 = 0
    for i in range(8):
        if i % 2 == 0:
            tmp_1 += int(decode[i])
        else:
            tmp_2 += int(decode[i])
    answer = (tmp_1*3) + tmp_2
    if answer % 10:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {sum(map(int, decode))}')