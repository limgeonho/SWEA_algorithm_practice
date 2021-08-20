import sys
sys.stdin = open('input.txt')


def check_line(board):
    global answer
    for i in range(9):
        if sum(board[i]) != 45:
            answer = 0
            return


T = int(input())

for tc in range(1, T+1):
    board = []
    answer = 1
    for _ in range(9):
        board.append(list(map(int, input().split())))

    # 가로줄 검사
    check_line(board)
    # 뒤집기
    changed = list(zip(*board))
    # 다시 가로줄 검사
    check_line(changed)

    # 3*3 검사
    for i in range(0, 6, 3):
        for j in range(0, 6, 3):
            tmp = 0
            for k in range(3):
                for l in range(3):
                    tmp += board[i+k][j+l]
            if tmp != 45:
                answer = 0
                break

    print(f'#{tc} {answer}')