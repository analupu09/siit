# sa se scrie un program care gestioneaza o lista de masini. o masina este reprezentata ca dictionar si contine urmatoarele chei:
# id (identificator unic) - se va genera de catre program (il generati programatic)
# brand
# model
# hp (horse power)
# price

import random
import string
import json

s: int = 10

cars = [
    {
        'id': ''.join(random.choices(string.ascii_uppercase + string.digits, k=s)),
        'brand': 'Volkswagen',
        'model': 'Arteon',
        'horse_power': 190,
        'price': 9876
    },
    {
        'id': ''.join(random.choices(string.ascii_uppercase + string.digits, k=s)),
        'brand': 'Opel',
        'model': 'Astra',
        'horse_power': 62,
        'price': 1254
    },
    {
        'id': ''.join(random.choices(string.ascii_uppercase + string.digits, k=s)),
        'brand': 'Volkswagen',
        'model': 'Golf',
        'horse_power': 210,
        'price': 7565
    },
    {
        'id': ''.join(random.choices(string.ascii_uppercase + string.digits, k=s)),
        'brand': 'Skoda',
        'model': 'Octavia',
        'horse_power': 95,
        'price': 4595
    },
    {
        'id': ''.join(random.choices(string.ascii_uppercase + string.digits, k=s)),
        'brand': 'Ford',
        'model': 'Puma',
        'horse_power': 110,
        'price': 2876
    },
    {
        'id': ''.join(random.choices(string.ascii_uppercase + string.digits, k=s)),
        'brand': 'Skoda',
        'model': 'Fabia',
        'horse_power': 95,
        'price': 989
    },
    {
        'id': ''.join(random.choices(string.ascii_uppercase + string.digits, k=s)),
        'brand': 'Ford',
        'model': 'Mustang',
        'horse_power': 120,
        'price': 4.500
    },
    {
        'id': ''.join(random.choices(string.ascii_uppercase + string.digits, k=s)),
        'brand': 'Opel',
        'model': 'Corsa',
        'horse_power': 55,
        'price': 750
    }
]

print('cars', cars)

# masinile sunt catalogate in functie de numarul de cai putere astfel:
# slow_Cars - masinile cu numarul de cai putere < 120
# fast_cars - masinile cu numarul de cai putere >= 120, dar < 180
# sport_cars - masinile cu numarul de cai putere >= 180

horse_power_list = []


def type_horse_power(item):
    return item['horse_power']


for car in cars:
    if type_horse_power(car):
        horse_power_list.append(car)

horse_power_list = list(filter(lambda item: item['horse_power'] < 120, cars))
print('slow_cars', horse_power_list)
horse_power_list = list(filter(lambda item: item['horse_power'] >= 120 < 180, cars))
print('fast_cars', horse_power_list)
horse_power_list = list(filter(lambda item: item['horse_power'] > 180, cars))
print('sport_cars', horse_power_list)


# masinile sunt catalogate in functie de pret astfel:
# cheap - masinile cu pretul < 1000
# medium - masinile cu pretul >= 1000, dar < 5000
# expensive - masinile cu pretul >= 5000

car_price_list = []


def cars_price(item):
    return item['price']


for car in cars:
    if cars_price(car):
        car_price_list.append(car)

car_price_list = list(filter(lambda item: item['price'] < 1000, cars))
print('cheap: ', car_price_list)
car_price_list = list(filter(lambda item: item['price'] >= 1000 < 5000, cars))
print('medium: ', car_price_list)
car_price_list = list(filter(lambda item: item['price'] >= 5000, cars))
print('expensive: ', car_price_list)
