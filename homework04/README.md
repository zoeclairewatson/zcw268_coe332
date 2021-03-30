
# Homework 4: Midterm Project

The purpose of this project is to build upon homework 2, where one script generated a JSON file of assembled animals and another one that read in and printed one animal at random, as well as incorporating a new breeding feature. Furthermore, homework 3 developed a Flask app (app.py is the python script) to access the generated JSON file of animals(animals_data.json), including routes to access specific data relating to the animals within the file. A Dockerfile has been written to containerize the Flask app, and a consumer file has been written for peers to consume this data. Building onto this even more, homework 4 connects the Flask app to a Redis database & incorporates new routes to provide further complexity to functionality.

## Installation

Install this project by cloning the repository, then navigating to the homework04 directory. For example:

```bash
git clone https://github.com/zoeclairewatson/zcw268_coe332.git
cd homework04
```

## Running the Code

This directory already has the JSON file of assembled animals included.

## Docker Image

You can build a Docker image using the provided docker-compose.yml file within this directory. Use the command:

```bash
docker-compose -p zoeclairewatson -d
```

## Curl the Port

Route to establish Redis database:

```bash
curl localhost:5037/establish
```

Route to return all animals:

```bash
curl localhost:5037/animals
```

Route to return all animals with a specified head:

```bash
curl localhost:5037/animals/head?head='<nameofanimal>'
```

For example, to return animals with bunny heads:

```bash
curl localhost:5037/animals/head?head='bunny'
```

Route to return all animals with a specified number of legs:

```bash
curl localhost:5037/animals/legs?num_legs=<integernumber>
```

For example, to return animals with 6 legs:

```bash
curl localhost:5037/animals/legs?num_legs=6
```

Route to create one random animal:

```bash
curl localhost:5037/animals/random
```

Route to select an animal by UUID:

```bash
curl localhost:5037/animals/uid?uid='<uuid>'
```

For example:

```bash
curl localhost:5037/animals/uid?uid='db354f4c-3274-4aba-a3fc-b7c8b56ace05'
```

Route to select animal by UUID and specify updates to its information:

```bash
curl localhost:5037/animals/edit?head='<nameofanimal>'&body='<nameofanimal>'&num_arms=<integernumber>&num_legs=<integernumber>&num_tails=<integernumber>&uid='<uuid>'
```

For example:

```bash
curl localhost:5037/animals/edit?head='snake'&body='clam-bass'&num_arms=4&num_legs=8&num_tails=2&uid='db354f4c-3274-4aba-a3fc-b7c8b56ace05'
```

Route to return a total count of the animals:

```bash
curl localhost/5037:/animals/total_count
```

Route to select a range of animals by date:

```bash
curl localhost:5037/animals/dates?begin='2021-03-30 02:32:21.976033'&end='2021-03-31 02:32:21.969637'
```

Route to delete a range of animals by date:


```bash
curl localhost:5037/animals/deletion?begin='2021-03-30 02:32:21.976033'&end='2021-03-31 02:32:21.969637'
```

Route to return the average number of legs per animal:

```bash
curl localhost:5037/animals/averagelegs
```


## Consumer File

This file provides URLs for others to consume this data.
