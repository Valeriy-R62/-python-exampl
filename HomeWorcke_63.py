class  Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000
    def horse_powers(self, power):
        self.power = power
        return (self.power)

class Nissan(Vehicle,Car):
    vehicle_type = "sedan"
    price = 2300000
    power = 180
    Car.horse_powers(Car,power=180)

nissan1 = Nissan()
print(f'тип {Nissan.vehicle_type}')
print(f'Цена {Nissan.price}')
print(f'Мощность {nissan1.power}')


