import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    forth = list(input().split())
    stack = []

    try:
        for s in forth:
            if s == '.':
                answer = stack.pop()
                if len(stack) != 0:
                    answer = 'error'
                    break
            elif s == '+':
                stack.append(stack.pop(-2) + stack.pop(-1))
            elif s == '-':
                stack.append(stack.pop(-2) - stack.pop(-1))
            elif s == '*':
                stack.append(stack.pop(-2) * stack.pop(-1))
            elif s == '/':
                stack.append(int(stack.pop(-2) / stack.pop(-1)))
            else:
                stack.append(int(s))
    except:
        answer = 'error'

    print(f'#{tc} {answer}')
