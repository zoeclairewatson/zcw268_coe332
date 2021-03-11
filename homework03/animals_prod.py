#!/usr/bin/env python3
import json
import petname
import random
import sys
import datetime

bizarre_animals = []

def add_animals(animal):
    bizarre_animals.append(animal)

animal_head_list = ['snake', 'bull', 'lion', 'raven', 'bunny']

for x in range(100):

    head = animal_head_list[random.randint(0, 4)]

    body1 = petname.name()
    body2 = petname.name()
    body = body1 + '-' + body2

    num_arms = random.randrange(2, 11, 2)

    num_legs = random.randrange(3, 13, 3)

    num_tails = num_arms + num_legs

    creation_time = str(datetime.datetime.now())

    animal = {}

    animal['head'] = head
    animal['body'] = body
    animal['arms'] = num_arms
    animal['legs'] = num_legs
    animal['tails'] = num_tails
    animal['timestamp'] = creation_time

    add_animals(animal)

with open('animals_data.json', 'w') as write_file:
    json.dump(bizarre_animals, write_file, indent=2)
