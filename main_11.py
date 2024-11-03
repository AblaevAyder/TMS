from classes_11 import MyTime, SuperStr, Car

time1 = MyTime(1,1,1)
time2 = MyTime(time1)
time3 = MyTime("10:10:10")

print(time1)
print(time2)
print(time3)
print(time1 == time3)
print()

super_str = SuperStr("adada")
print(super_str)
print(super_str.is_palindrom())
print(super_str.is_repeatance("a"))
print()

car1 = Car("MARK1", "MODEL", 2001)
print(car1)
car1.low_speed()
print(car1.speed)
car1.add_speed()
car1.turn()
print(car1.speed)
car1.stop()
print(car1.year)
