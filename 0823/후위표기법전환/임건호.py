import sys
sys.stdin = open('input.txt')

tmp = input()

stack = []
answer = []
priority = {'+': 1, '*': 2, '/': 2}

for s in tmp:
    if s.isdigit():
        answer.append(s)
    else:
        while stack and priority[stack[-1]] > priority[s]:
            answer.append(stack.pop())
        stack.append(s)

while stack:
    answer.append(stack.pop())

print(''.join(answer))