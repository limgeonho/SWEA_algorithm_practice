import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    # start와 end 시간입력
    time = []

    for _ in range(n):
        s, e = map(int, input().split())
        time.append((s, e))

    # end시간을 기준으로 오름차순 정렬
    changed = sorted(time, key = lambda x:x[1])

    # 가능한 후보의 첫번째 요소 입력
    candidate = [changed[0]]

    # 입력된 후보들 중 마지막 후보의 끝나는 시간과 다음 요소의 시작시간을 비교해서 후보목록에 추가
    for i in range(1, len(changed)):
        if candidate[-1][1] <= changed[i][0]:
            candidate.append(changed[i])

    print(f'#{tc} {len(candidate)}')