from random import *

from car import Car
from evcar import EvCar

my_car = Car("Toyota", "Esquire", 2018)
print(my_car.get_description())

my_car.update_odometer(42200)
my_car.read_odometer()

my_car.increament_odometer(30)
my_car.read_odometer()

my_car.update_odometer(42200)
my_car.increament_odometer(-30)

my_ev_car = EvCar("BMW", "X7", 2023, 160)
print(my_ev_car.get_description())
my_ev_car.describe_battery()

random_num = randint(0, 10)
print(random_num)

arr = ["a1", "a2", "a3", "a4", "a5"]
print(choice(arr))