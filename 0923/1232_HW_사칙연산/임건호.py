import sys
sys.stdin = open('input.txt')

############################## 재귀함수 ##############################

def check(node, x):
    # 해당하는 연산자, 왼쪽, 오른쪽 자식이 있다면 할당 없으면 error가 아닌 0(.get())
    operator, left, right = node.get(x, 0)
    left = int(left)
    right = int(right)

    # 왼쪽 자식 => 또 다른 연산자를 만남
    if len(node[left]) != 1:
        left = check(node, left)
    # 그냥 값만 존재하면 왼쪽자식에 할당
    else:
        left = int(node.get(left)[0])

    # 오른쪽 자식 => 또 다른 연산자를 만남
    if len(node[right]) != 1:
        right = check(node, right)
    # 그냥 값만 존재하면 왼쪽자식에 할당
    else:
        right = int(node.get(right)[0])

    # 연산
    if operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    elif operator == '*':
        return left * right
    else:
        return left // right

for tc in range(1, 11):
    n = int(input())
    node = {}
    for _ in range(n):
        array = list(map(str, input().split()))
        # 노드번호를 key값으로 넣고 나머지를 value로 설정
        node[int(array[0])] = array[1:]

    answer = check(node, 1)
    print(f'#{tc} {answer}')


############################## ? ##############################

for tc in range(1, 11):
    n = int(input())
    tree = [[0]]
    for _ in range(n):
        tree.append(list(map(str, input().split())))

    # sort()하지 않으면 무작위로 입력값이 주어진 경우에는 error가 발생
    tree.sort(key=lambda x:int(x[0]))
    for i in range(n, 0, -1):
        node = tree[i]
        if len(node) == 4:
            # 연산자를 포함하고 있는경우 => node[2], node[3]이 왼쪽, 오른쪽 자식노드
            left, right = int(tree[int(node[2])][1]), int(tree[int(node[3])][1])

            if node[1] == '+':
                tree[i] = [i, left + right]
            elif node[1] == '-':
                tree[i] = [i, left - right]
            elif node[1] == '*':
                tree[i] = [i, left * right]
            else:
                tree[i] = [i, left // right]

    print(f'#{tc} {tree[1][1]}')

# 재귀함수 : 0.010970592498779297
# ? : 0.009974956512451172)