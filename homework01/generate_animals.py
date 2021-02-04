import json

import petname

import random

animal_head_list = ['snake', 'bull', 'lion', 'raven', 'bunny']

bizarre_animals = {}
bizarre_animals['animals'] = []

for x in range(20):
    
    head = animal_head_list[random.randint(0, 4)]

    body1 = petname.name()
    body2 = petname.name()
    body = body1 + '-' + body2

    num_arms = random.randrange(2, 11, 2)

    num_legs = random.randrange(3, 13, 3)

    num_tails = num_arms + num_legs

    bizarre_animals['animals'].append( {'head': head, 'body': body, 'arms': num_arms, 'legs': num_legs, 'tails': num_tails} )

with open('animals.json', 'w') as out:
    json.dump(bizarre_animals, out, indent=2)
