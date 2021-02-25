#!/usr/bin/env python3
import json

import random

import sys

#new functionality: to breed 2 random animals and add resulting animal to dictionary
def new_functionality_breeding(bizarre_animals):
    
    #generate elements of a random animal from bizarre_animals dictionary for parent 1
    parent1_index = random.randint(0,19)

    parent1 = bizarre_animals['animals'][parent1_index]
    parent1_head = bizarre_animals['animals'][parent1_index]['head']
    parent1_body = bizarre_animals['animals'][parent1_index]['body'] 
    parent1_arms = bizarre_animals['animals'][parent1_index]['arms']
    parent1_legs = bizarre_animals['animals'][parent1_index]['legs']
    parent1_tails = bizarre_animals['animals'][parent1_index]['tails']

    #generate elements of a random animal from bizarre_animals dictionary for parent 2
    parent2_index = random.randint(0,19)

    parent2 = bizarre_animals['animals'][parent2_index]
    parent2_head = bizarre_animals['animals'][parent1_index]['head'] 
    parent2_body = bizarre_animals['animals'][parent1_index]['body']
    parent2_arms = bizarre_animals['animals'][parent1_index]['arms']
    parent2_legs = bizarre_animals['animals'][parent1_index]['legs']
    parent2_tails = bizarre_animals['animals'][parent1_index]['tails']    
    
    #mixx the parents elements to generate a new animal
    new_animal_head = random.choice([parent1_head, parent2_head])
    new_animal_body = random.choice([parent1_body, parent2_body])
    new_animal_arms = int(round((parent1_arms + parent2_arms) / 2))
    new_animal_legs = int(round((parent1_legs + parent2_legs) / 2))
    new_animal_tails = int(round((parent1_tails + parent2_tails) / 2))

    #add newly bred animal to bizarre_animals dictionary, with the addition of its parents
    bizarre_animals['animals'].append( {'head': new_animal_head, 'body': new_animal_body, 'arms': new_animal_arms, 'legs': new_animal_legs, 'tails': new_animal_tails, '1st parent': parent1, '2nd parent': parent2} )

#main function
def main():

    #open animals.json and read file
    with open('animals.json', 'r') as f:
        animals = json.load(f)

    #print one animal at random to screen
    random_index = random.randint(0,19)
    print("Random Animal: ", animals['animals'][random_index])

    #print blank line for readability
    print()

    #call new function for breeding
    new_functionality_breeding(animals)

    #print new randomly bred animal to screen
    print("Newly Bred Animal: ", animals['animals'][20])

if __name__ == '__main__':
    main()
