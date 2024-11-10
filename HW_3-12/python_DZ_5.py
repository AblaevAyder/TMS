
# Задание № 2
print("Задание № 2")
money = 10000
k = 300
days = 0
money_count = 0

while money_count < money:
    days += 1
    if days % 7 != 0:
        money_count += k

print(f"Маша накопила {money} за {days} дней в итоге = {money_count}")
print()

# Задание № 3
print("Задание № 3")
n = 6
fibo_1 = 0
fibo_2 = 1
fibo_summ = 0

if n == 1 :
    print(f"{n} член последовательности фибоначчи равен 1")
else:
    for ind in range(n - 1):
        fibo_summ = fibo_1 + fibo_2
        fibo_1 = fibo_2
        fibo_2 = fibo_summ
    print(f"{n} член последовательности фибоначчи равен {fibo_summ}")

print()

# Задание № 4
print("Задание № 4 ")
number_list = [1, 2, 3, 4, 5]
number_summ = 0
number_max = number_list[0]
number_min = number_list[0]

for number in number_list:
    number_summ += number
    if number > number_max:
        number_max = number
    elif number < number_min:
        number_min = number

print(f"Сумма всех силел списка равна {number_summ}")
print(f"Минимальное число = {number_min} \n Максимальное число = {number_max}")
print()

# Задание № 5
print("Задание № 5")
number_list_1 = [1, 1, 2, 2, 3, 4, 9, 10, 2, 5]
number_list_1.sort()
number_set = set(number_list_1)
number_count = 0

for num in number_set:
    number_count = number_list_1.count(num)
    print(f"{num} встречается {number_count} раз")

print()

# Задание № 6/7
print("Задание № 6/7")
number_list_1 = [1, 2, 3, 4, 9, 10, 5]
number_list_1.sort()
find_number = 10
low = 0
high = len(number_list_1) - 1

while low <= high:
    mid = (low + high) // 2
    guess = number_list_1[mid]
    if guess < find_number:
        low = mid + 1
    elif guess > find_number:
        high = mid - 1
    elif guess == find_number:
        print(f"Искомый элемент {find_number} находится под индексом {mid}")
        break
    else:
        print(f"Искомый элемент не найден")

print()



