"""
 Урок 6. Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

 Урок 6. Задание 5.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, name: str, color: str, speed: int = 0, is_police: bool = False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            return f"едет"
        else:
            return f"стоит"

    def stop(self):
        if self.speed == 0:
            return f"остановилась"
        else:
            return f"в движении"

    def turn(self, direction: str):
        if direction == "налево":
            return f"{direction}"
        else:
            return f"не {direction}"

    def show_speed(self):
        return f"{self.speed} km/h"


class TownCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color, speed)

    def show_speed(self):
        if self.speed > 60:
            print(f"TownCar превышает 60 km/h")
        return f"{self.speed} km/h"


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color, speed)

    def show_speed(self):
        if self.speed > 40:
            print(f"TownCar превышает 40 km/h")
        return f"{self.speed} km/h"


class PoliceCar(Car):
    pass


john_car = Car("BMW", "black", 30, False)
artur_car = Car("Ford", "black", 50, True)

police_car = PoliceCar("Уаз", "black", 0, True)
town_car = TownCar("Уаз", "black", 80)
sport_car = SportCar("Fera", "red", 100, False)
work_car = WorkCar("Toyota", "black", 50)

print(f"Авто {john_car.name}, цвета {john_car.color}"
      f" {john_car.go()} {john_car.stop()} направление"
      f" {john_car.turn('налево')} со скоростью {john_car.show_speed()}")

print(f"Авто {artur_car.name}, цвета {artur_car.color}"
      f" {artur_car.go()} {artur_car.stop()} направление"
      f" {artur_car.turn('налево')} со скоростью {artur_car.show_speed()}")

print(f"Авто {police_car.name}, цвета {police_car.color}"
      f" {police_car.go()} {police_car.stop()} направление"
      f" {police_car.turn('налево')} со скоростью {police_car.show_speed()}")

print(f"Авто {town_car.name}, цвета {town_car.color}"
      f" {town_car.go()} {town_car.stop()} направление"
      f" {town_car.turn('налево')} со скоростью {town_car.show_speed()}")

print(f"Авто {sport_car.name}, цвета {sport_car.color}"
      f" {sport_car.go()} {sport_car.stop()} направление"
      f" {sport_car.turn('налево')} со скоростью {sport_car.show_speed()}")

print(f"Авто {work_car.name}, цвета {work_car.color}"
      f" {work_car.go()} {work_car.stop()} направление"
      f" {work_car.turn('налево')} со скоростью {work_car.show_speed()}")
