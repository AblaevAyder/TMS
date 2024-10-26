import time
from functools import reduce

# Задание № 1
print("Задание № 1")

lst = [1, 1, 2, 3, 4, 0, -2, -3]

lst_1 = map(lambda x: str(x), lst)

print(list(lst_1))
print()

# Задание № 2
print("Задание № 2")

lst_2 = filter(lambda x: x > 0, lst)

print(list(lst_2))

# Задание № 3
print("Задание № 3")

list_str = ["abcba", "asdf", "dffd"]
def is_polindrom(str: str):

    for ind in range(len(str)):

        if str[ind] == str[len(str) - 1 - ind]:
            pass

        else:
            return False

    return True

print(list(filter(is_polindrom, list_str)))


# Задание № 4
print("Задание № 4")
import time
def timer(function):

    def wrapper():
        print("Выполнение функции")
        start_time = time.perf_counter_ns()
        function()
        print(f"Время выполнения функции",time.perf_counter_ns() - start_time)


    return wrapper

@timer
def printer():
    print("HELLO WORLD")

printer()

# Задание № 5
print("Задание № 5")

from functools import reduce

rooms = [
{"name": "Kitchen", "length": 6, "width": 4},
{"name": "Room 1", "length": 5.5, "width": 4.5},
{"name": "Room 2", "length": 5, "width": 4},
{"name": "Room 3", "length": 7, "width": 6.3},
]

rooms_ploshad = list(map(lambda x: list(x.values())[1] * list(x.values())[2], rooms))

ploshad = reduce(lambda x, y: x + y, rooms_ploshad)

print(f"Площади комнат = {rooms_ploshad}")
print(f"Площадь квартиры = {ploshad}")

