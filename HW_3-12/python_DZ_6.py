
from random import random

# Задание № 1
print("Задание № 1")
number_list_1 = [1, 2, 3, 4, 9, 10, 5] # Вводимый список
num = 5 # Искомый эллемент
number_list_1.sort()
ln = len(number_list_1)

def b_search(list_1: list[int], num, low = 0, higt = ln):

    if (higt < low):
        return "Не найдено"

    else:
        mid = low + ((higt - low) // 2)

        if list_1[mid] > num:
            return b_search(list_1, num, low, mid - 1)

        elif list_1[mid] < num:
            return b_search(list_1, num, mid + 1, higt)

        else:
            return mid

print(f"Эллемент {num} находиться под индексом {b_search(number_list_1, num)}")
print()

# Задание № 2
print("Задание № 2")

binary = []
number = 15

def num_to_binary(num):
    if num < 1:
        binary.append(num)
        return num
    else:
        num_to_binary(num // 2)
        binary.append(num % 2)
        return num

num_to_binary(number)
print(f"{number} в двоичной системе = ", end = "")

for i in binary:
    print(i, end="")

print(end="\n")
print()

# Задание № 3
print("Задание № 3")
num = 24

def is_simple(num: int):
    if num == 1:
        return "Не простое число"

    for i in range(2, num):

        if num % i == 0:
            return "Не простое число"

    return "Простое число"

print(is_simple(num))
print()

# Задание № 4
print("Задание № 4")

def higt_div(a, b):
    if a == 0 or b == 0:
        return "У нуля не может быть НОД"

    if a % b == 0:
        return b

    elif b % a == 0:
        return a

    for i in range(1, a if a <= b else b):

        if a % i == 0 and b % i == 0:
            num = i

    return num

print(higt_div(12, 18))
print()

# Задание № 5
print("Задание № 5")
str = "ABCD"

def shifr(a: str, step = 1, b = True):
    string = ""

    if b :

        for letter in a:
            string += chr(ord(letter) + step)

    else:
        for letter in a:
            string += chr(ord(letter) - step)

    return string

print(f"Зашифрованная строка {str} = {shifr(str)}")
print(f"Расшифрованная строка {str} = {shifr(str, False)}")
print()

# Задание № 7
print("Задание № 7")
from random import random # Для того, чтобы запускать выделением

def make_matrix(row: int, coll: int):
    matrix = []

    for i in range(row):
        matrix.append([])
        for j in range(coll):
            matrix[i].append(int(random() * 100))

    return matrix

matrix = make_matrix(3, 3)
print(matrix)
print()

# Задание № 8
print("Задание № 8")

def find_min_max(matrix: list):
    min = matrix[0][0]
    max = matrix[0][0]

    for row in matrix:
        for i in row:

            if i >= max:
                max = i

            elif i <= min:
                min = i

    return f"Min эллемент матрицы = {min} \nMax эллемент матрицы = {max}"

for row in matrix:
    print(row)

print(find_min_max(matrix))
print()

# Задание № 9
print("Задание № 9")

def matrix_summ(matrix: list):
    summa = 0
    summa_1 = 0

    for row in matrix:
        for i in row:
            summa += i

    print(f"Сумма всех эллементов матрицы = {summa}")
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            summa_1 += matrix[j][i]

        print(f"Доля {i+1} столбца = {round(summa_1 / summa * 100)}%")
        summa_1 = 0

    return None

matrix_summ(matrix)
print()

# Задание № 12
print("Задание № 12")

num_h = int(random() * 100)

def find_num_matrix(matrix: list, num: int):
    for i in range(len(matrix[0])):
        count = 0

        for j in range(len(matrix)):

            if matrix[j][i] == num:
                count += 1

        if count > 0:
            print(f"В {i + 1} столбце {num} присутствует {count} раз")

        else:
            print(f"в {i + 1} столбце {num} отсутствует")

find_num_matrix(matrix, num_h)
print()

# Задание № 13
print("Задание № 13")

def matrix_diagon(matrix: list):
    summa_main = 0
    summa_peref = 0

    for i in range(len(matrix)):
        summa_main += matrix[i][i]
        summa_peref += matrix[i][len(matrix) - 1 - i]

    print(f"Сумма главной диагонали = {summa_main}")
    print(f"Сумма побочной диагонали = {summa_peref}")

    return None

matrix_diagon(matrix)
print()

# Задание № 14
print("Задание № 14")
matrix_1 = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 1],
]

def matrix_odd(matrix: list):

    for row in matrix:

        if row.count(1) % 2 == 0:
            row.append(0)

        else:
            row.append(1)

    return matrix

for row in matrix_odd(matrix_1):
    print(row)