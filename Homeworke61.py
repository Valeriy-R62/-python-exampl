class Car:

    price = 1000000
    def horse_powers(self):
        print('50')

class Nissan(Car):

    price = 1500000

    def horse_powers(self):
        print('120')

class Kia(Car):

    price = 800000

    def horse_powers(self):
        print('70')

car = Car()
print(car.price)
car.horse_powers()
nissan = Nissan()
print(nissan.price)
nissan.horse_powers()
kia = Kia()
print(kia.price)
kia.horse_powers()

