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

#clear out redis and pull data from json file into redis database
@app.route('/establish', methods=['GET'])
def establish_database():
    rd = redis.StrictRedis(host='redis', port=6379, db=8)
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

#route to return all animals
@app.route('/animals', methods=['GET'])
def get_animals():
    return json.dumps(get_data())

#pull data from Redis database and put it into a dictionary
def get_data():
    
    rd = redis.StrictRedis(host='redis', port=6379, db=8)

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

    #data from redis is now stored in a dictionary
    return bizarre_animals

    #old method - data retrieval from json file
    #with open("/app/animals_data.json", "r") as json_file:
    #    bizarre_animals = json.load(json_file)
    #return bizarre_animals

#route to randomly generate one animal
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

#route to return all animals with a specified head
@app.route('/animals/head', methods=['GET'])
def get_animal_head():
    head = request.args.get('head')
    test = get_data()
    return json.dumps([x for x in test if x['head'] == head])

#route to return all animals with a specified number of legs
@app.route('/animals/legs', methods=['GET'])
def get_animal_legs_num():
    num_legs = int(request.args.get('num_legs'))
    test = get_data()
    return json.dumps([x for x in test if x['legs'] == num_legs])

#route to return an animal resulting from breeding
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
    resulting_animal['arms'] = int(round((int(parent1['arms']) + int(parent2['arms'])) / 2))
    resulting_animal['legs'] = int(round((int(parent1['legs']) + int(parent2['legs'])) / 2))
    resulting_animal['tails'] = resulting_animal['arms'] + resulting_animal['legs']
    resulting_animal['creation time'] = str(datetime.datetime.now())
    resulting_animal['uid'] = str(uuid.uuid4())
    return resulting_animal

#route to query a range of dates
@app.route('/animals/dates', methods=['GET'])
def query_dates():

    #request string type start and end dates of range 
    start = request.args.get('start')
    end = request.args.get('end')

    #use datetime.datetime.strptime to convert from string to datetime 
    #use yyyy/mm/dd (m-month, d-day, y-year) followed by hh:mm:ss.ffffff (h-hours, m-minutes, s-seconds, f-microseconds) formatting
    date_start = datetime.datetime.strptime(start, "'%Y-%m-%d_%H:%M:%S.%f'")
    date_end = datetime.datetime.strptime(end, "'%Y-%m-%d_%H:%M:%S.%f'")

    test = get_data()

    #returns all animals with creation time both after the start date and before the end date
    #(as long as a creation time exists)
    
    date_range = []

    date_range = [x for x in test if ( x['creation time'] != 'None' and ( datetime.datetime.strptime( x['creation time'], '%Y-%m-%d %H:%M:%S.%f' ) <= date_end and datetime.datetime.strptime( x['creation time'], '%Y-%m-%d %H:%M:%S.%f' ) >= date_start ))]

    return json.dumps(date_range)

#route to select a particular animal by its UUID
@app.route('/animals/uid', methods=['GET'])
def get_animal_uid():
    uid = request.args.get('uid')
    test = get_data()
    return json.dumps([x for x in test if x['uid'] == uid])

#route to edit a creature by passing its UUID and updating qualities
@app.route('/animals/testing', methods=['GET'])
def test_edit_animal():
    
    update = {}

    #request new information for update
    animal_uid = request.args.get('uid')
    update['head'] = str(request.args.get('head'))
    update['body'] = str(request.args.get('body'))
    update['arms'] = str(request.args.get('arms'))
    update['legs'] = str(request.args.get('legs'))
    update['tails'] = str(request.args.get('tails'))
    update['creation time'] = str(datetime.datetime.now())
    update['uid'] = str(animal_uid)

    rd = redis.StrictRedis(host='redis', port= 6379, db=8)

    test = get_data()

    specified_animal = [x for x in test if x['uid'] == str(animal_uid)]

    rd.hmset(test.index(specified_animal[0]), json.dumps(update))
    
    test = get_data()

    return json.dumps([x for x in test if x['uid'] == str(animal_uid)])

#route to edit a creature by passing its UUID and updating qualities
@app.route('/animals/update', methods=['GET'])
def edit_animal():

    #request new information for update
        #convert each entry to string to resolve DataError (NoneType)
    animal_uid = request.args.get('uid')
    update_head = str(request.args.get('head'))
    update_body = str(request.args.get('body'))
    update_arms = str(request.args.get('arms'))
    update_legs = str(request.args.get('legs'))
    update_tails = str(request.args.get('tails'))
    update_time = str(datetime.datetime.now())
    update_uid = str(animal_uid)

    test = get_data()

    rd = redis.StrictRedis(host= 'redis', port=6379, db=8)

    for x in range (0, len(test)):
        
        if( test[x]['uid'] == animal_uid):

            if update_head != 'None':
                rd.hset(x, 'head', update_head)
                
            if update_body != 'None':
                rd.hset(x, 'body', update_body)

            if update_arms != 'None':
                rd.hset(x, 'arms', update_arms)

            if update_legs != 'None':
                rd.hset(x, 'legs', update_legs)

            if update_tails != 'None':
                rd.hset(x, 'tails', update_tails)

            rd.hset(x, 'creation time', update_time)
            rd.hset(x, 'uid', update_uid)
                   
    test = get_data()
    
    return json.dumps([x for x in test if x['uid'] == update_uid])





#    rd.hset(test.index(specified_animal[0]), 'head', update_head)
#    rd.hset(test.index(specified_animal[0]), 'body', update_body)
#    rd.hset(test.index(specified_animal[0]), 'arms', update_arms)
#    rd.hset(test.index(specified_animal[0]), 'legs', update_legs)
#    rd.hset(test.index(specified_animal[0]), 'tails', update_tails) 
#    rd.hset(test.index(specified_animal[0]), 'creation time', update_time)
#    rd.hset(test.index(specified_animal[0]), 'uid', update_uid)

#    test = get_data()

#    return json.dumps([x for x in test if x['uid'] == animal_uid])


#route to delete a selection of animals by date range
@app.route('/animals/deletions', methods=['GET'])
def delete_selection():

    rd = redis.StrictRedis(host='redis', port=6379, db=8)

    #request string type start and end dates of range
    start = request.args.get('start')
    end = request.args.get('end')

    #use datetime.datetime.strptime to convert from string to datetime
    #use yyyy/mm/dd (m-month, d-day, y-year) followed by hh:mm:ss.ffffff (h-hours, m-minutes, s-seconds, f-microseconds) formatting
    date_start = datetime.datetime.strptime(start, "'%Y-%m-%d_%H:%M:%S.%f'")
    date_end = datetime.datetime.strptime(end, "'%Y-%m-%d_%H:%M:%S.%f'")

    test = get_data()

    #returns all animals with creation time both after the start date and before the end date
    #(as long as a creation time exists)
    
    date_range = []
    
    date_range = [x for x in test if ( x['creation time'] != 'None' and ( datetime.datetime.strptime( x['creation time'], '%Y-%m-%d %H:%M:%S.%f' ) <= date_end and datetime.datetime.strptime( x['creation time'], '%Y-%m-%d %H:%M:%S.%f' ) >= date_start ))]

    #go through each animal in date_range list
    for x in range (0, len(date_range)):
        
        #delete each key:value for each animal (x) from database
        #rd.hdel() removes specified fields from the hash stored at the key
        rd.hdel(x, 'head')
        rd.hdel(x, 'body')
        rd.hdel(x, 'arms')
        rd.hdel(x, 'legs')
        rd.hdel(x, 'tails')
        rd.hdel(x, 'creation time')
        rd.hdel(x, 'uid')

    return json.dumps(get_data())

#route to return the avergage number of legs per animal
@app.route('/animals/averagelegs', methods=['GET'])
def average_legs():

    animal_count = 0
    legs_count = 0

    test = get_data()

    for x in range (0, len(test)):
        animal_count = animal_count + 1

        rd = redis.StrictRedis(host= 'redis', port=6379, db=8)

        x_legs = int(rd.hget(x, 'legs'))
        legs_count = legs_count + x_legs

    average_legs = str((legs_count) / (animal_count))

#route to return the total count of animals
@app.route('/animals/total', methods=['GET'])
def total_animals():
    
    total_count = 0
  
    test = get_data()
 
    for x in range(0, len(test)):

        total_count = total_count + 1

    return str(total_count)

    return average_legs

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

