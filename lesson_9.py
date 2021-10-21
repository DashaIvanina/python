#5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Ручка')

class Pencil(Pen):
    def draw(self):
        print('Карандаш')

class Handle(Pencil):
    def draw(self):
        print('Маркер')

pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()


#2
class Road:
    def __init__(self, lenght, widht):
        self._lenght = lenght
        self._widht = widht

    def weight(self):
        return (self._lenght * self._widht * 25 * 5 / 1000)

r = Road(20, 5000)
print(r.weight(), 'т')

#3
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']

class Position(Worker):
    def get_full_name(self):
        return (f'{self.name} {self.surname}')

    def get_total_income(self):
        return self._income_wage + self._income_bonus


p = Position('Даша', 'Иванина', 'Поломойка', {'wage': 1000, 'bonus': 100})
print(p.get_full_name())
print(p.get_total_income())


#4
class Car:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} едет')

    def stop(self):
        print(f'{self.name} стоит')

    def turn(self, direction):
        print('{} поворачивает {}'.format(self.name, direction))

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('скорость превышена')
        else:
            print('скорость' + self.speed)


class SportCar(Car):
    pass


class WorkCar(TownCar):
    def show_speed(self):
        if self.speed > 40:
            print('скорость превышена')
        else:
            print('скорость' + self.speed)


class PoliceCar(Car):
    pass


c = Car(80, 'red', 'lada', True)
c.go()
c.stop()
c.turn('влево')
c.show_speed()

t = TownCar(100, 'blue', 'opel', False)
t.show_speed()

w = WorkCar(45, 'white', 'maz', True)
w.show_speed()

s = SportCar(100, 'blue', 'opel', False)
s.turn('вправо')

