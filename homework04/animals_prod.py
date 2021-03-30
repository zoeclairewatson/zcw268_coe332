#!/usr/bin/env python3
import json
import petname
import random
import sys
import datetime
import uuid

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

    timestamp = str(datetime.datetime.now())

    animal = {}

    animal['head'] = head
    animal['body'] = body
    animal['arms'] = num_arms
    animal['legs'] = num_legs
    animal['tails'] = num_tails
    animal['creation time'] = timestamp
    animal['uuid'] = str(uuid.uuid4())

    add_animals(animal)

with open('animals_data.json', 'w') as write_file:
    json.dump(bizarre_animals, write_file, indent=2)
