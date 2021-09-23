import sys
sys.stdin = open('input.txt')

# def check(node, x):
#     operator, left, right = node.get(x)
#     left = int(left)
#     right = int(right)
#
#     if len(node[left]) != 1:
#         left = check(node, left)
#     else:
#         left = int(node.get(left)[0])
#
#     if len(node[right]) != 1:
#         right = check(node, right)
#     else:
#         right = int(node.get(right)[0])
#
#     if operator == '+':
#         return left + right
#     elif operator == '-':
#         return left - right
#     elif operator == '*':
#         return left * right
#     else:
#         return left // right
#
# for tc in range(1, 11):
#     n = int(input())
#     node = {}
#     for _ in range(n):
#         array = list(map(str, input().split()))
#         node[int(array[0])] = array[1:]
#
#     answer = check(node, 1)
#     print(f'#{tc} {answer}')


for tc in range(1, 11):
    n = int(input())
    tree = [[0]]
    for _ in range(n):
        tree.append(list(map(str, input().split())))

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