import json

import random

import sys

#new functionality: to breed 2 random animals and add resulting animal to dictionary
def new_functionality_breeding(bizarre_animals):

    parent1_index = random.randint(0,19)

    parent1 = bizarre_animals['animals'][parent1_index]
    parent1_head = bizarre_animals['animals'][parent1_index]['head']
    parent1_body = bizarre_animals['animals'][parent1_index]['body'] 
    parent1_arms = bizarre_animals['animals'][parent1_index]['arms']
    parent1_legs = bizarre_animals['animals'][parent1_index]['legs']
    parent1_tails = bizarre_animals['animals'][parent1_index]['tails']

    parent2_index = random.randint(0,19)

    parent2 = bizarre_animals['animals'][parent2_index]
    parent2_head = bizarre_animals['animals'][parent1_index]['head'] 
    parent2_body = bizarre_animals['animals'][parent1_index]['body']
    parent2_arms = bizarre_animals['animals'][parent1_index]['arms']
    parent2_legs = bizarre_animals['animals'][parent1_index]['legs']
    parent2_tails = bizarre_animals['animals'][parent1_index]['tails']    
    
    new_animal_head = random.choice([parent1_head, parent2_head])
    new_animal_body = random.choice([parent1_body, parent2_body])
    new_animal_arms = (parent1_arms + parent2_arms) / 2
    new_animal_legs = (parent1_legs + parent2_legs) / 2
    new_animal_tails = (parent1_tails + parent2_tails) / 2

    bizarre_animals['animals'].append( {'head': new_animal_head, 'body': new_animal_body, 'arms': new_animal_arms, 'legs': new_animal_legs, 'tails': new_animal_tails, '1st parent': parent1, '2nd parent': parent2} )

def main():

    with open('animals.json', 'r') as f:
        animals = json.load(f)

    random_index = random.randint(0,19)
    print("Random Animal: ", animals['animals'][random_index])

    new_functionality_breeding(animals)

    print("Newly Bred Animal: ", animals['animals'][20])

if __name__ == '__main__':
    main()
