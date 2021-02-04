import json

import random

with open('animals.json', 'r') as f:
    animals = json.load(f)

random_index = random.randint(0,19)
print(animals['animals'][random_index])
