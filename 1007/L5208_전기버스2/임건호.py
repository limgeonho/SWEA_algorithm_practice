import sys
sys.stdin = open('input.txt')


def dfs(pos):
    global answer, cnt
    # 현재 위치가 목적지의 위치보다 크다면 종료(갈 수 있는 거임)
    if pos >= need_to_go:
        # 해당 횟수가 최소 횟수라면 갱신
        if answer > cnt:
            answer = cnt
        return

    # 현재까지의 충전횟수가 최소횟수보다 크다면 종료(백트래킹)
    if answer <= cnt:
        return

    # 버스가 현재 갈 수 있는 에너지
    energy = array[pos]

    # 가지고 있는 에너지에서 갈 수 있는 지점을 dfs
    for i in range(energy, 0, -1):
        cnt += 1
        dfs(i+pos)
        cnt -= 1


T = int(input())

for tc in range(1, T+1):
    array = list(map(int, input().split()))
    # 목적지
    need_to_go = array[0]
    # 충전횟수
    cnt = 0
    # 최소충전횟수
    answer = 2147000000

    dfs(1)

    print(f'#{tc} {answer-1}')