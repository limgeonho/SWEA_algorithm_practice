import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    calculator = input()
    tmp_answer = []
    tmp_nums = []
    answer = []

    for s in calculator:
        if s == '*':
            tmp_answer.append(s)
        elif s == '+':
            while tmp_answer:
                tmp_nums.extend(tmp_answer.pop())
            tmp_answer.append(s)
        else:
            tmp_nums.append(s)

    while tmp_answer:
        tmp_nums.extend(tmp_answer.pop())

    for s in tmp_nums:
        if s == '+':
            tmp_2 = answer.pop()
            tmp_1 = answer.pop()
            answer.append(int(tmp_2) + int(tmp_1))
        elif s == '*':
            tmp_2 = answer.pop()
            tmp_1 = answer.pop()
            answer.append(int(tmp_2) * int(tmp_1))
        else:
            answer.append(int(s))
    print(f'#{tc} {answer[0]}')