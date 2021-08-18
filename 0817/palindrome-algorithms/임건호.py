import sys
import time
sys.stdin = open('input-long.txt')


def is_palindrome_1(s):
    if s[:] == s[::-1]:
        return True
    return False


def is_palindrome_2(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    # s = input()
    s = 'a' * 10000000
    start_1 = time.time()

    if is_palindrome_1(s):
        print("palindrome")
    else:
        print("no...")

    end_1 = time.time()

    print(f'is_palindrome_1() : {end_1 - start_1}')


# ==================================================

    start_2 = time.time()

    if is_palindrome_2(s):
        print("palindrome")
    else:
        print("no...")

    end_2 = time.time()

    print(f'is_palindrome_2() : {end_2 - start_2}')

    print("==================================================")