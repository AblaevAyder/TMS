
def my_gen(stop = 0):
    counter = 0
    number = 0
    while counter < stop:
        number += 1
        counter += 1
        if number == 4:
            number = 1
        yield number

number = int(input("Введите количество членов последательности"))

generator = my_gen(number)

for i in generator:
    print(i, end = " ")

