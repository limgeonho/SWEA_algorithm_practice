import sys
sys.stdin = open('input.txt')

def cook(arr):
    tmp = 0
    for i in range(n//2):
        for j in range(i+1, n//2):
            tmp += recipe[arr[i]][arr[j]] + recipe[arr[j]][arr[i]]
    return tmp

# dfs탐색해서 모든 경우 탐색
def dfs(L, start):
    global answer
    if L == n//2:
        A = []
        B = []
        # 구한 조합을 바탕으로 A와 B요리를 나눔
        for i in range(n):
            if check[i]:
                A.append(i)
            else:
                B.append(i)
        # 각각의 요리의 값을 구함
        a = cook(A)
        b = cook(B)
        # 최소값으로 갱신
        tmp = abs(a-b)
        if tmp < answer:
            answer = tmp
        return answer

    # 조합을 구하는 과정
    for i in range(start, n):
        if not check[i]:
            check[i] = True
            dfs(L+1, i+1)
            check[i] = False


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    recipe = [list(map(int, input().split())) for _ in range(n)]
    answer = sys.maxsize
    check = [False] * n
    dfs(0,0)

    print(f'#{tc} {answer}')