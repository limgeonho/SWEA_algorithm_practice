import sys
sys.stdin = open('input.txt')


def search(array, target, start, end):
    global flag
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
            if flag == 'R':
                return False
            flag = 'R'
        else:
            start = mid + 1
            if flag == 'L':
                return False
            flag = 'L'
    return None

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))
    arr_1.sort()

    answer = 0
    for num in arr_2:
        flag = 0
        if search(arr_1, num, 0, len(arr_1)-1):
            answer += 1
    print(f'#{tc} {answer}')