import csv
import os
import json

# Задание № 5
print("Задание № 5")

# Функция вывода json файла в формате csv
def read_json():
    with open("employees.json", "r") as json_file:
        json_data = json.load(json_file)
        print("Так будет выглядеть json файл в формате csv")
        print(", ".join(json_data[0].keys()))

        for data in json_data:
            for val in data.values():
                print(val, end=", ")
            print()

# Функция преобразование из json в csv файл
def json_to_csv():
    with open("employees.json", "r") as json_file:
        with open("employees_csv.csv", "w") as csv_file:
            json_data = json.load(json_file)
            csv_writer = csv.DictWriter(csv_file, delimiter = ",", lineterminator="\r", fieldnames = json_data[0].keys())
            csv_writer.writeheader()

            for data in json_data:
                csv_writer.writerow(data)

# Функция добавление нового сотрудника
def json_data_add():
    with open("employees.json", "r") as json_file:
        json_data = json.load(json_file)
        json_data.append({})

        for key in json_data[0].keys():
            new = input(f"Введите {key} сотрудника ")
            new_data = {}
            try:
                if key == "height":
                    new = int(new)
                elif key == "weight":
                    new = float(new)
                elif key == "car":
                    if new == "true" or int(new) == 1:
                        new = True
                    elif new == "false" or int(new) == 0:
                        new = False
                elif key == "languages":
                    new = new.split(",")
            except Exception:
                print("Некорректный ввод")
                break
            new_data.update({key: new})

        json_data[len(json_data) - 1].update(new_data)

    with open("employees.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)

# Функция поиска по имени
def find_name_json():
    with open("employees.json", "r") as json_file:
        json_data = json.load(json_file)
        find_name = input("Введите искомое имя: ")

        for data in json_data:
            if data["name"] == find_name:
                print(data)
                break
        else:
            print("Искомое имя не найдено")

# Функция поиска по ЯП
def find_languages():
    find_lan = input("Введите искомый ЯП: ")
    with open("employees.json", "r") as json_file:
        json_data = json.load(json_file)
        for data in json_data:
            if find_lan in data['languages']:
                print(data["name"])

# Функция поиска по году
def find_year():
    find_input = int(input("Введите год: "))
    with open("employees.json", "r") as json_file:
        json_data = json.load(json_file)
        count = 0
        all_height = 0
        for data in json_data:
            if find_input > int(data['birthday'].split(".")[2]):
                all_height += data["height"]
                count += 1

    if count == 0:
        print("Все младше введенного года")
    else:
        print(f"Средний рост всех кто старше этого года = {all_height//count}")


while True:
    print("""Выберите задачу (введите число)
    1. Пренести данные из .json в .csv формат
    2. Добавить сотрудника
    3. Поиск по имени
    4. Поиск по ЯП
    5. Средний рост старше введенного года
    6. Вывести .json файл в формате .csv 
    0. Завершить работу
    """)
    value = input()
    if value == "1":
        json_to_csv()
    elif value == "2":
        json_data_add()
    elif value == "3":
        find_name_json()
    elif value == "4":
        find_languages()
    elif value == "5":
        find_year()
    elif value == "6":
        read_json()
    elif value == "0":
        break
    else:
        print("Некорректный ввод, попытайтесь еще раз ")

