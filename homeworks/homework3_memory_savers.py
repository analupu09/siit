# sa se scrie un program care gestioneaza o lista de masini. o masina este reprezentata ca dictionar si contine urmatoarele chei:
# id (identificator unic) - se va genera de catre program (il generati programatic)
# brand
# model
# hp (horse power)
# price

import random
import string
from typing import List, Union, Dict
s: int = 10

cars = [
    {
        'id': ''.join(random.choices(string.ascii_uppercase + string.digits, k=s)),
        'brand': 'Volkswagen',
        'model': 'Arteon',
        'horse_power': 180,
        'price': 6.989
    },
    {
        'id': ''.join(random.choices(string.ascii_uppercase + string.digits, k=s)),
        'brand': 'Skoda',
        'model': 'Fabia',
        'horse_power': 95,
        'price': 999
    },
    {
        'id': ''.join(random.choices(string.ascii_uppercase + string.digits, k=s)),
        'brand': 'Ford',
        'model': 'Mustang',
        'horse_power': 120,
        'price': 4.500
    }
]

print(cars)

