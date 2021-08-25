import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    nV, nE = map(int, input().split())
    edge = []
    for i in range(nE):
        edge.append(input().split())

    dic = {}
    for j in range(1, nV+1):
        temp = []
        for i in range(nE):
            if edge[i][0] == str(j):
                temp.append(edge[i][1])
        dic[str(j)] = temp

    st, go = map(int,input().split())

    visit = [0]*(nV+1)
    visit[st] = 1
    que = [str(st)]
    while(que):
        curr = que.pop(0)
        for i in dic[curr]:
            if visit[int(i)] != 1:
                que.append(i)
                visit[int(i)] = 1

    print(dic)
    flag = 1 if visit[go] == 1 else 0
    print('#%d %d' % (test_case, flag))