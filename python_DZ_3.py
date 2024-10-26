import math

# ЗАДАНИЕ №1
print("Задание № 1")
x = 1
y = 2
z = 3
print(f"{x} + {y} + {z} =", x + y + z)
print(f"{x} - {y} - {z} =", x - y - z)
print(f"{x} * {y} * {z} =", x * y * z)
print(f"{x} - {y} + {z} =", x - y + z)
print(f"{x} * {y} / {z} =", x * y / z)
print(f"({x} + {y}) % {z} =", (x + y) % z)
print()

# ЗАДАНИЕ №2
print("Задание № 2")
cat_a = 3
cat_b = 4
print(f"Площадь треугольника с катетами {cat_a} и {cat_b} равна ", cat_a * cat_b / 2)
print(f"Гипотенуза равна ", math.sqrt(cat_a ** 2 + cat_b ** 2))
print()

# ЗАДАНИЕ №3
print("Задание № 3")
str_1 = "Hello world"
str_2 = "a b c"
str_3 = "test"
str_4 = "test1 test2 test3 test4 test5"
print(f"В {str_1} = {len(str_1.split())} слов")
print(f"В {str_2} = {len(str_2.split())} слов")
print(f"В {str_3} = {len(str_3.split())} слов")
print(f"В {str_4} = {len(str_4.split())} слов")
print()

# Задание №4
print("Задание № 4")
str_h = "hhhabchghhh"
print(str_h)
h_1 = str_h.find("h")
h_2 = str_h.rfind("h")

str_h = str_h[0:h_1+1] + str_h[h_1+1:h_2].replace("h","H") + str_h[h_2::]

print(str_h)
print()

# Задание №5
print("Задание № 5")
string_1 = "Hello"
string_2 = "TEST-STR"
print(string_1[2], string_2[2])
print(string_1[-2], string_2[-2])
print(string_1[0:5], string_2[0:5])
print(string_1[0:-2], string_2[0:-2])
print(string_1[0::2], string_2[0::2])
print(string_1[1::2], string_2[1::2])
print(string_1[::-1], string_2[::-1])
print(string_1[-1::-2], string_2[-1::-2])
print(len(string_1), len(string_2))
print()

# Задание №6
print("Задание № 6")
a = 200
b = 123
c = 587
print(f"Последняя цифра числа {a} = {a % 10}")
print(f"Последняя цифра числа {b} = {b % 10}")
print(f"Последняя цифра числа {c} = {c % 10}")
print()

# Задание №7
print("Задание № 7")
a_1 = 123
b_1 = 978
print(f"Кол-во десятков в числе {a_1} = {(a_1 % 100) // 10}")
print(f"Кол-во десятков в числе {b_1} = {(b_1 % 100) // 10}")
print()

# Задание №8
print("Задание № 8")
a_2 = 555
print(f"Сумма цифр в числе {a_2} = {(a_2 // 100) + ((a_2 % 100) // 10) + ((a_2 % 100) % 10)}")
print(f"Сумма цифр в числе {a_1} = {(a_1 // 100) + ((a_1 % 100) // 10) + ((a_1 % 100) % 10)}")