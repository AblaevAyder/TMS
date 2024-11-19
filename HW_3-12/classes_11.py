
class MyTime:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        if isinstance(hours, MyTime):
            self.hours = hours.hours
            self.minutes = hours.minutes
            self.seconds = hours.seconds

        elif isinstance(hours, str):
            args = hours.split(":")
            self.hours = int(args[0])
            self.minutes = int(args[1])
            self.seconds = int(args[2])

        else:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds


    @staticmethod
    def get(hours, minutes, seconds):
        if len(str(hours)) == 1:
            hours = "0" + str(hours)
        else:
            hours = str(hours)

        if len(str(minutes)) == 1:
            minutes = "0" + str(minutes)
        else:
            minutes = str(minutes)

        if len(str(seconds)) == 1:
            seconds = "0" + str(seconds)
        else:
            seconds = str(seconds)

        return f"{hours}:{minutes}:{seconds}"

    def __str__(self):
        return MyTime.get(self.hours, self.minutes, self.seconds)

    def __mul__(self, other):
        hours = ((self.hours * other) + ((self.minutes * other) // 60) + ((self.seconds * other) // 3600)) % 24
        minutes = (self.minutes * other + ((self.seconds * other) // 60)) % 60
        seconds = (self.seconds * other) % 60
        return MyTime.get(hours, minutes, seconds)

    def __add__(self, other):
        hours = ((self.hours + other.hours) + ((self.minutes + other.minutes) // 60) + ((self.seconds * other.seconds) // 3600)) % 24
        minutes = (self.minutes + other.minutes + ((self.seconds + other.seconds) // 60)) % 60
        seconds = (self.seconds + other.seconds) % 60
        return MyTime.get(hours, minutes, seconds)

    def __sub__(self, other):
        hours = ((self.hours - other.hours) + ((self.minutes - other.minutes) // 60) + ((self.seconds - other.seconds) // 3600)) % 24
        minutes = ((self.minutes - other.minutes) + ((self.seconds - other.seconds) // 60)) % 60
        seconds = (self.seconds - other.seconds) % 60
        return MyTime.get(hours, minutes, seconds)

    # ==
    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds
    # !=
    def __ne__(self, other):
        return self.hours != other.hours or self.minutes != other.minutes or self.seconds != other.seconds
    # <
    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours and self.minutes < other.minutes:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds < other.seconds:
            return True
        else:
            return False
    # <=
    def __le__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours and self.minutes < other.minutes:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds < other.seconds:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return True
        else:
            return False
    # >
    def __gt__(self, other):
        if self.hours > other.hours:
            return True
        elif self.hours == other.hours and self.minutes > other.minutes:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds > other.seconds:
            return True
        else:
            return False
    # >=
    def __ge__(self, other):
        if self.hours > other.hours:
            return True
        elif self.hours == other.hours and self.minutes > other.minutes:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds > other.seconds:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return True
        else:
            return False


class Car:
    def __init__(self, mark, model, year, speed = 0):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed

    def __str__(self):
        return f"{self.__mark} {self.__model}, {self.__year}"

    def stop(self):
        self.__speed = 0

    def add_speed(self):
        self.__speed += 5

    def low_speed(self):
        self.__speed -= 5

    def turn(self):
        self.__speed *= -1

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, value):
        self.__mark = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value


class SuperStr(str):
    def __init__(self, string):
        self.string = string

    def is_repeatance(self, param):
        if len(self.string) % len(param) == 0 and self.string.count(param) == len(self.string) / len(param):
            return True
        else:
            return False

    def is_palindrom(self):

        for ind in range(len(self.string)):

            if self.string[ind] == self.string[len(self.string) - 1 - ind]:
                pass

            else:
                return False

        return True
