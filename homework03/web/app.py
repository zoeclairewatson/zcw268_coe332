import json
import petname
import random

from flask import Flask, request

app = Flask(__name__)

@app.route('/helloworld', methods=['GET'])
def hello_world():
    return "Hello World!!\n"

@app.route('/animals', methods=['GET'])
def get_animals():
    return json.dumps(get_data())

def get_data():
    with open("/app/animals_data.json", "r") as json_file:
        bizarre_animals = json.load(json_file)
    return bizarre_animals

@app.route('/animals/random', methods=['GET'])
def create_random():
    create_animal = generate_random()
    return json.dumps(create_animal)

def generate_random():
    head_choices = ['snake', 'bull', 'lion', 'raven', 'bunny']
    random_animal = {}
    random_animal['head'] = head_choices[random.randint(0,4)]
    random_animal['body'] = petname.name() + '-' + petname.name()
    random_animal['arms'] = random.randrange(2,11,2)
    random_animal['legs'] = random.randrange(3,13,3)
    random_animal['tails'] = random_animal['arms'] + random_animal['legs']
    return random_animal

@app.route('/animals/head', methods=['GET'])
def get_animal_head():
    head = request.args.get('head')
    test = get_data()
    return json.dumps([x for x in test if x['head'] == head])

@app.route('/animals/legs', methods=['GET'])
def get_animal_legs_num():
    num_legs = int(request.args.get('num_legs'))
    test = get_data()
    return json.dumps([x for x in test if x['legs'] == num_legs])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

