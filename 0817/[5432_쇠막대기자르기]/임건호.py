import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1, T+1):
    steel = input()
    stack = []
    answer = 0

    for i in range(len(steel)):
        if steel[i] == '(':
            stack.append(steel[i])
        else:
            stack.pop()
            # 레이저
            if steel[i-1] == '(':
                answer += len(stack)
            # 막대기 끝
            elif steel[i-1] == ')':
                answer += 1

    print(f'#{tc} {answer}')

































