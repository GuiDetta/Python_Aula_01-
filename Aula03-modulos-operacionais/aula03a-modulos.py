import math

from sympy.crypto import bifid10

num = 4
raiz = math.sqrt(num)
print(f"A raiz de {num} é {raiz:.2f}")

graus = 90
radiano = graus / 180 * math.pi
seno = math.sin(radiano)
print(f"O seno é {seno}")

import random

num_rand = random.random()
print(num_rand+10)

num_rand_int = random.randint(1, 10)
print(num_rand_int)