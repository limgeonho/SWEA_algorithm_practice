import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    array = list(map(int, input().split()))
    check = 0
    while True:

        if check == 1:
            break
        for i in range(5):
            tmp = array.pop(0) - (i+1)
            # print(tmp)
            if tmp <= 0:
                tmp = 0
                check = 1
                array.append(tmp)
                break
            array.append(tmp)

    print(f'#{tc}', end=' ')
    print(*array)