# Задание № 1
print("Задание № 1")

try:
    rost = float(input("Введите рост в метрах"))
    ves = float(input("Введите вес в киллограммах"))

    if ves <= 0:
        print("Вес не может быть меньше или равно 0")

    imt = round(ves / (rost ** 2))
    print(f"Рост = {rost} м., Вес = {ves} кг.")

    if 0 < imt <= 18:
        print(f"ИМТ = {imt} - Дефицит массы тела")

    elif 18 < imt <= 25:
        print(f"ИМТ = {imt} - Норма")

    elif 25 < imt <= 30:
        print(f"ИМТ = {imt} - Предожирение")

    elif 30 < imt <= 35:
        print(f"ИМТ = {imt} - Ожирение 1 степени")

    elif 35 < imt <= 40:
        print(f"ИМТ = {imt} - Ожирение 2 степени")

    elif 40 < imt:
        print(f"ИМТ = {imt} - Ожирение 3 степени")

except ValueError:
    print("Вы ввели не число")

except ZeroDivisionError:
    print("Рост не может быть 0")

except Exception:
    print("Что-то пошло не так")

# Задание № 2
print("Задание № 2")

try:
    num_1 = int(input("Введите первое целое число"))
    num_2 = int(input("Введите второе целое число"))
    sigil = input("Введите оператор")

    if sigil == "-":
        print(f"Ответ {num_1} - {num_2} = {num_1 - num_2}")

    elif sigil == "+":
        print(f"Ответ {num_1} + {num_2} = {num_1 + num_2}")

    elif sigil == "*":
        print(f"Ответ {num_1} * {num_2} = {num_1 * num_2}")

    elif sigil == "/":
        print(f"Ответ {num_1} / {num_2} = {num_1 / num_2}")

    else:
        print("Некорректный оператор")

except ValueError:
    print("Введены не числа")

except ZeroDivisionError:
    print("На 0 делить нельзя")

except Exception:
    print("Что-то пошло не так")
