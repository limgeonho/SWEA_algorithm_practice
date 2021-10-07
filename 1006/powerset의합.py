# powerset의 합

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
for i in range(1<<n):
    total = 0
    answer = []
    for j in range(n):
        if i & (1<<j):
            answer.append(arr[j])
            total += arr[j]
            if total > 10:
                continue
    if total == 10:
        print(answer)