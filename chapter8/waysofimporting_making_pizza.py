#  this a way for importing pizzas.
import pizza

pizza.make_pizza(18, 'pineapple')
pizza.make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')

import pizza as p
p.make_pizza(18, 'pineapple')
p.make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza

make_pizza(18, 'pineapple')
make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza as mp

mp(18, 'pineapple')
mp(15, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import *

make_pizza(18, 'pineapple')
make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')