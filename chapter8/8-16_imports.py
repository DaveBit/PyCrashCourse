import car_function
from car_function import make_car
from car_function import make_car as mc
import car_function as cf
from car_function import *

#  import car_function
car = car_function.make_car('Volkswage', 'Passat', color='red', navigator=True)
print(car)

#  from car_function import make_car
car = make_car('Volkswage', 'Passat', color='red', navigator=True)
print(car)

#  from car_function import make_car as mc
car = mc('Volkswage', 'Passat', color='red', navigator=True)
print(car)

#  import car_function as cf
car = cf.make_car('Volkswage', 'Passat', color='red', navigator=True)
print(car)

#  from car_function import *
car = make_car('Volkswage', 'Passat', color='red', navigator=True)
print(car)