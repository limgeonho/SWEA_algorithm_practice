import sys
sys.stdin = open('input.txt')

# def dfs(L, total):
#     global answer
#     if L == n:
#         if total > answer:
#             answer = total
#             return
#     # 백트래킹
#     if total <= answer:
#         return
#
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = True
#             dfs(L+1, total * array[L][i] / 100)
#             visited[i] = False
#
# T = int(input())
#
# for tc in range(1, T+1):
#     n = int(input())
#     array = [list(map(int, input().split())) for _ in range(n)]
#     visited = [False] * n
#     answer = 0
#     dfs(0, 1)
#     print(f'#{tc} {answer*100:.6f}')

for t in range(int(input())):
    # 직원 수
    n = int(input())
    # 가능한 전체 경우의 수
    m = 1<<n

    d = [0]*m
    
    # 소수로 변환해서 입력받기
    p = [[*map(lambda x:x/100,map(int,input().split()))] for _ in range(n)]

    d[0] = 1
    for mask in range(m):
        x = sum(1 for i in range(n) if mask&(1<<i))
        for j in range(n):
            if mask&(1<<j) == 0:
                d[mask|(1<<j)] = max(d[mask|(1<<j)],d[mask]*p[x][j])
    print(f'#{t+1} {d[-1]*100:.6f}')