import sys
sys.stdin = open('input.txt')

# 행렬 90도로 뒤집기...=> 2*3 행렬처럼 row와 col이 달라도 가능
def change(array):
    row = len(array)
    col = len(array[0])

    res = [[0] * row for _ in range(col)]
    # changed는 사실 불필요한 과정이지만 출력 조건 때문에.. 억지로 끼워넣기
    changed = [[0] for _ in range(row)]

    for r in range(row):
        for c in range(col):
            res[c][row-1-r] = array[r][c]

    for i in range(row):
        tmp = ''.join(res[i])
        changed[i] = tmp

    return changed


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    matrix = []
    final_matrix = []
    for _ in range(n):
        matrix.append(list(map(str, input().split())))

    for _ in range(3):
        matrix = change(matrix)
        final_matrix.append(matrix)

    print(f'#{tc}')
    for i in range(n):
        for j in range(3):
            print(final_matrix[j][i], end=' ')
        print()