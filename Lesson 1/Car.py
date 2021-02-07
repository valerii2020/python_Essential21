class Car:
    fuel = None # топливо в авто
    S = None # пройденое растояние

    def fuel_on(self):
        car.fuel = int(input('Введите колличество заправленого топлива '))
        return

    def ride(self):
        for i in range(car.fuel):
            car.S = car.S + 10
        return car.S

car = Car()
car.fuel = 0
car.S = 0

car.fuel_on()
car.ride()

print('на заправленом топливе машина проехала ', car.S, 'километров')
