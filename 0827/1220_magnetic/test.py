def rotate_matrix_by_90_degree_1(a):
    # 기존 행렬의 행과열의 순서를 바꿔야한다 : 행, 열 => 열, 행
    row_length = len(a)
    column_length = len(a[0])

    # 새로운 행렬의 기본 설정(기존의 행렬과는 반대)
    res = [[0] * row_length for _ in range(column_length)]

    # 오른쪽 위에서 부터 하나씩 아래로 채워나감
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res

array_1 = [[1,2,3],[1,2,3],[1,2,3]]
array_1 = rotate_matrix_by_90_degree_1(array_1)
array_1 = rotate_matrix_by_90_degree_1(array_1)

print(array_1)

array_2 = [[1,2,3],[1,2,3],[1,2,3]]
array_2 = list(zip(*array_2))
array_2 = list(zip(*array_2))
print(array_2)