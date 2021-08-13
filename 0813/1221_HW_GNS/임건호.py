import sys
sys.stdin = open('input.txt')

str_to_num = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
num_to_str = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}

T = int(input())

for tc in range(1, T+1):
    num, str_length = map(str, input().split())
    long_str = input()
    new_str = long_str.split(' ')

    for i in range(int(str_length)):
        new_str[i] = str_to_num[new_str[i]]
    changed_str = new_str[:-1]
    changed_str.sort()

    for i in range(len(changed_str)):
        changed_str[i] = num_to_str[changed_str[i]]

    print(f'#{tc}')
    print(*changed_str)
