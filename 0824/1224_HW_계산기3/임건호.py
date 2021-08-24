import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    n = int(input())
    form = input()
    answer = ''
    stack = []

    for s in form:
        if s.isdigit():
            answer += s
        else:
            if s == '+' or s == '-':
                if stack and (stack[-1] == '*' or stack[-1] == '/'):
                    answer += stack.pop()

                if stack and (stack[-1] == '+' or stack[-1] == '-'):
                    answer += stack.pop()

                stack.append(s)

            elif stack and (stack[-1] == '*' or stack[-1] == '/') and (s == '*' or s == '/'):
                answer += stack.pop()
                stack.append(s)
            elif s == '*' or s == '/':
                stack.append(s)
            elif s == '(':
                stack.append(s)
            elif s == ')':
                while stack[-1] != '(':
                    answer += stack.pop()
                stack.pop()
    while stack:
        answer += stack.pop()

    # priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    calculate = []
    final_answer = []
    for a in answer:
        if a.isdigit():
            final_answer.append(a)
        elif a == '+':
            tmp2 = int(final_answer.pop())
            tmp1 = int(final_answer.pop())
            tmp3 = tmp1 + tmp2
            final_answer.append(tmp3)
        elif a == '-':
            tmp2 = int(final_answer.pop())
            tmp1 = int(final_answer.pop())
            tmp3 = tmp1 - tmp2
            final_answer.append(tmp3)
        elif a == '*':
            tmp2 = int(final_answer.pop())
            tmp1 = int(final_answer.pop())
            tmp3 = tmp1 * tmp2
            final_answer.append(tmp3)
        elif a == '/':
            tmp2 = int(final_answer.pop())
            tmp1 = int(final_answer.pop())
            tmp3 = tmp1 // tmp2
            final_answer.append(tmp3)

    print(f'#{tc} {final_answer[0]}')
