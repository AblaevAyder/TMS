# Задание № 8
print("Задание № 8")
matrix = []
matrix_range = 4
num_1 = 100
for i in range(matrix_range):
    matrix.append([])
    for j in range(matrix_range):
        matrix[i].append(num_1)
        num_1 += 2

for row in matrix:
    print(row)
print()

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end = " ")
    print(end = "\n")

print()

trans_matrix = []
for i in range(len(matrix)):
    trans_matrix.append([])
    for j in range(len(matrix)):
        trans_matrix[i].append(matrix[j][i])
for row in trans_matrix:
    print(row)


