import os

# Задание № 1
print("Задание № 1")

print(os.name)
print(os.listdir())
print(os.getcwd())

# Задание № 2
print("Задание № 2")

with open("test.txt", "r") as file:
    file_lines = file.readlines()
    print(file_lines[0], end = "")
    print(file_lines[4], end = "")
    s_1 = 2
    s_2 = 5
    print()

    for x in range(0, 5):
        print(file_lines[x], end = "")

    print()

    for x in range(s_1 - 1, s_2):
        print(file_lines[x], end = "")

    print()

    for line in file_lines:
        print(line, end = "")

# Задание № 3
print("Задание № 3")

with open("some_test.txt", "w") as file:
    for x in range(6):
        file.write(input() + "\n")

# Задание № 4
print("Задание № 4")

with open("test.txt", "r") as first_file:
    with open("some_test.txt", "r") as second_file:
        first_file_lines = first_file.readlines()
        second_file_lines = second_file.readlines()
        for x in range(len(first_file_lines)):
            if first_file_lines[x] != second_file_lines[x]:
                print(f"Файлы не совпадают на {x + 1} строке")
                break
        else:
            print("Файлы совпадают")













