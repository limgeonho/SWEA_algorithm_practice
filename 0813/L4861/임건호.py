import sys
sys.stdin = open('input.txt')


def check(s):
    if s[:] == s[::-1]:
        return True
    return False


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]

    for i in range(len(words)):
        for j in range(len(words)-M+1):
            tmp_word_row = ''
            for k in range(M):
                tmp_word_row += words[i][j+k]
            if check(tmp_word_row):
                answer = tmp_word_row

    for i in range(len(words)-M+1):
        for j in range(len(words)):
            tmp_word_col = ''
            for k in range(M):
                tmp_word_col += words[i+k][j]
            if check(tmp_word_col):
                answer = tmp_word_col

    print(f'#{tc} {answer}')