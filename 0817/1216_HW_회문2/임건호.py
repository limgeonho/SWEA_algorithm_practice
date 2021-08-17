import sys
sys.stdin = open('input.txt')


def check(s):
    if s[:] == s[::-1]:
        return True
    return False


def find_palindrome(matrix, tmp):
    for k in range(100):
        for i in range(100, 1, -1):
            if tmp > i:
                break
            for j in range(100-i+1):
                if check(matrix[k][j:i+j]):
                    if tmp < len(matrix[k][j:i+j]):
                        tmp = len(matrix[k][j:i+j])
                        break
    return tmp


for tc in range(1, 11):
    T = int(input())
    words = [input() for _ in range(100)]
    tmp_row = 0
    tmp_col = 0
    changed_words = [[0] * 100 for _ in range(100)]

    # 가로 확인
    tmp_row = find_palindrome(words, tmp_row)

    # 행렬 뒤집기...
    for i in range(100):
        for j in range(100):
            changed_words[i][j] = words[j][i]

    # 세로 확인
    tmp_col = find_palindrome(changed_words, tmp_col)


    print(f'#{tc} {max(tmp_row, tmp_col)}')