import json
import petname
import random
import redis
import uuid
import datetime

from flask import Flask, request

app = Flask(__name__)

@app.route('/helloworld', methods=['GET'])
def hello_world():
    return "Hello World!!\n"

@app.route('/establish', methods=['GET'])
def establish_database():
    rd = redis.StrictRedis(host='redis', port=6379, db=0)
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
        animal['uid'] = str(uuid.uuid4())
        rd.hmset(x, animal)

    return "fresh database"

@app.route('/animals', methods=['GET'])
def get_animals():
    return json.dumps(get_data())

def get_data():
    rd = redis.StrictRedis(host='redis', port=6379, db=0)

    bizarre_animals = []
    
    for x in range(100):
    
        animal = {}
        animal['head'] = str(rd.hget(x, 'head'))
        animal['body'] = str(rd.hget(x, 'body'))
        animal['arms'] = str(rd.hget(x, 'arms'))
        animal['legs'] = str(rd.hget(x, 'legs'))
        animal['tails'] = str(rd.hget(x, 'tails'))
        animal['creation time'] = str(rd.hget(x, 'creation time'))
        animal['uid'] = str(rd.hget(x, 'uid'))

        bizarre_animals.append(animal)

    #with open("/app/animals_data.json", "r") as json_file:
        #bizarre_animals = json.load(json_file)

    return bizarre_animals

#randomly generate an animal
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
    random_animal['creation time'] = str(datetime.datetime.now())
    random_animal['uid'] = str(uuid.uuid4())
    return random_animal

#return all animals with specified head
@app.route('/animals/head', methods=['GET'])
def get_animal_head():
    head = request.args.get('head')
    test = get_data()
    return json.dumps([x for x in test if x['head'] == head])

#return all animals with specified number of legs
@app.route('/animals/legs', methods=['GET'])
def get_animal_legs_num():
    num_legs = int(request.args.get('num_legs'))
    test = get_data()
    return json.dumps([x for x in test if x['legs'] == num_legs])

#return bred animals
@app.route('/animals/breeding', methods=['GET'])
def result_of_breeding():
    parent1 = random.choice(get_data())
    parent2 = random.choice(get_data())
    resulting_animal = breed_animals(parent1, parent2)
    return json.dumps(resulting_animal)

#breeding functionality
def breed_animals(parent1, parent2):
    resulting_animal = {}
    resulting_animal['head'] = random.choice([parent1['head'], parent2['head']])
    resulting_animal['body'] = random.choice([parent1['body'], parent2['body']])
    resulting_animal['arms'] = int(round((parent1['arms'] + parent2['arms']) / 2))
    resulting_animal['legs'] = int(round((parent1['legs'] + parent2['legs']) / 2))
    resulting_animal['tails'] = int(round((parent1['tails'] + parent2['tails']) / 2))
    resulting_animal['creation time'] = str(datetime.datetime.now())
    resulting_animal['uid'] = str(uuid.uuid4())
    return resulting_animal

#selct an animal by a specified uid
@app.route('/animals/uid', methods=['GET'])
def get_animal_uid():
    animal_uid = request.args.get('uid')
    test = get_data()
    return json.dumps([x for x in test if x['uid'] == animal_uid])

#edits an existing animal, updating to specified stats
@app.route('/animals/edit', methods=['GET'])
def edit_existing_animal():
    
    update_animal = {}

    #request new information to update
    update_animal['head'] = request.args.get('head')
    update_animal['body'] = request.args.get('body')
    update_animal['arms'] = request.args.get('arms')
    update_animal['legs'] = request.args.get('legs')
    update_animal['tails'] = request.args.get('tails')
    update_animal['updat time'] = str(datetime.datetime.now())
    animal_uid = str(request.args.get('uid'))

    test = get_data()
    
    rd = redis.StrictRedis(host='redis', port=6379, db=0)

    specified_animal = [x for x in test if x['uid'] == animal_uid]
    
    rd.hmset(bizarre_animals[specified_animals], update_animal)

    test = get_data()

    return json.dumps([x for x in test if x['uid'] == animal_uid])

#return a total count of animals
@app.route('/animals/total_count', methods=['GET'])
def get_total_count():
    animal_count = 0
    test = get_data()
    for x in range(0, len(bizarre_animals)):
        animal_count = animal_count + 1
    return str(animal_count)

#return average number of legs per animal
@app.route('/animals/averagelegs', methods=['GET'])
def get_average_legs():
    animal_count = 0
    leg_count = 0
    test = get_data()
    
    for x in range(0, len(bizarre_animals)):
        animal_count = animal_count + 1
        animal = bizarre_animals[x]
        leg_count = leg_count + int(animal['legs'])

    average = int(round(leg_count / animal_count))
    return str(average)

#query a range of dates
@app.route('/animals/dates', methods=['GET'])
def query_dates():
    begin = request.args.get('begin')
    begin_date = datetime.datetime.strptime(begin, "'%Y/%m/%d/-%H:%M:%S.%f'")
    end = request.args.get('end')
    end_date = datetime.datetime.strptime(end,"'%Y/%m/%d/-%H:%M:%S.%f'")

    test = get_data()
    
    return ([x for x in test if (datetime.datetime.strptime(x['creation time'], '%Y/%m/%d/-%H:%M:%S.%f') >= begin_date and datetime.datetime.strptime(x['creation time'], '%Y/%m/%d/-%H:%M:%S.%f') <= end_date)])   

#deletes a selection of animals by a date range
@app.route('/animals/deletion', methods=['GET'])
def delete_selection():
    begin = request.args.get('begin')
    begin_date = datetime.datetime.strptime(begin, "'%Y/%m/%d/-%H:%M:%S.%f'")
    end = request.args.get('end')
    end_date = datetime.datetime.strptime(end,"'%Y/%m/%d/-%H:%M:%S.%f'")

    test = get_data() 

    rd = redis.StrictRedis(host='redis', port=6379, db=0)

    deletions = []
    deletions = [x for x in test if (datetime.datetime.strptime(x['creation time'], '%Y/%m/%d/-%H:%M:%S.%f') >= begin_date and datetime.datetime.strptime(x['creation time'], '%Y/%m/%d/-%H:%M:%S.%f') <= end_date)] 

    for x in range(0, len(deletions)):
        delete_indices = test.index(deletions[x])
        rd.delete(delete_indices)

    return json.dumps(deletions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

