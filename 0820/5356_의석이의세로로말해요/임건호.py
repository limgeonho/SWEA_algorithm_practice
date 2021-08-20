import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    words = []
    max_length = 0
    answer = ''

    for _ in range(5):
        tmp = input()
        max_length = max(max_length, len(tmp))
        words.append(tmp)

    for i in range(5):
        if len(words[i]) != max_length:
            cnt = max_length - len(words[i])
            words[i] += cnt * '#'

    for i in range(max_length):
        for j in range(5):
            answer += words[j][i]

    answer = answer.replace('#', '')
    print(f'#{tc} {answer}')