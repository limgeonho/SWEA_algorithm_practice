import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

for _ in range(10):
    tc = int(input())
    str1 = input()
    long_str = input()
    answer = long_str.count(str1)

    print(f'#{tc} {answer}')