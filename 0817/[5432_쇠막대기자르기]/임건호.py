import sys
sys.stdin=open("input.txt")

# 레이저는 ()처럼 바로 연결되어야 한다.

T = int(input())

for tc in range(1, T+1):
    steel = input()
    # 다음시간에 배울 stack
    stack = []
    answer = 0

    for i in range(len(steel)):
        # 쇠막대기일지 레이저일지 모르기 때문에 바로 stack에 push
        if steel[i] == '(':
            stack.append(steel[i])
        # 입력값으로 )가 오는 경우
        else:
            stack.pop()
            # 레이저 => 바로 앞에 있던 괄호가 '(' 라면 레이저
            if steel[i-1] == '(':
                # 레이저가 기존에 존재하던 막대기들을 잘라버림
                answer += len(stack)
            # 막대기 끝 => 바로 앞에 있던 괄호가 '(' 이 아니라면 기존에 있던 막대기 한 개가 끝
            elif steel[i-1] == ')':
                # 막대기 한 개가 끝난 것이기 때문에 +1
                answer += 1

    print(f'#{tc} {answer}')

































