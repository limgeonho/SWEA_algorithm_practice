# 퀵정렬
# [11, 45, 23, 81, 28, 34]
# [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
# [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    left = []
    right = []
    pivot = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([11, 45, 23, 81, 28, 34]))
print(quick_sort([11, 45, 22, 81, 23, 34, 99, 22, 17, 8]))
print(quick_sort([1, 1, 1, 1, 1, 0, 0, 0, 0, 0]))