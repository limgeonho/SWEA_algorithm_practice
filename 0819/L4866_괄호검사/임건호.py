import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    words = input()
    stack = []
    answer = 1
    for word in words:
        if word == '(' or word == '{':
            stack.append(word)
        elif word == ')' or word == '}':
            if len(stack) == 0:
                answer = 0
                break
            elif word == ')' and stack.pop() == '{':
                answer = 0
                break
            elif word == '}' and stack.pop() == '(':
                answer = 0
                break
    if len(stack):
        answer = 0

    print(f'#{tc} {answer}')