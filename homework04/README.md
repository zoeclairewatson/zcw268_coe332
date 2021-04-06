
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

```
```bash
docker-compose -p zoeclairewatson build
```

To run the container:

```bash
docker-compose -p zoeclairewatson up -d
```

## Curl the Port

Route to return all animals:

```bash
curl localhost:5037/animals
```

Route to return a randomly generated animal:

```bash
curl localhost:5037/animals/random
```

Route to return all animals with a specified head:

```bash
curl localhost:5037/animals/head?head='<nameofanimal>'
```

For example, to return animals with bull heads:

```bash
curl localhost:5037/animals/head?head='bull'
```

Route to return all animals with a specified number of legs:

```bash
curl localhost:5037/animals/legs?legs=<integernumber>
```

For example, to return animals with 6 legs:

```bash
curl localhost:5037/animals/legs?legs=6
```

Route to return an animal resulting from breeding:

```bash
curl localhost:5037/animals/breeding
```

Route to select a range of animals by date:

```bash
curl "localhost:5037/animals/dates?start='<yyyy-mm-dd_hh:mm:ss.ffffff>'&end='<yyyy-mm-dd_hh:mm:ss.ffffff>'"
```

For example:

```bash
curl "localhost:5037/animals/dates?start='2021-04-06_02:45:29.356846'&end='2021-04-06_02:45:29.381785'"
```

Route to select an animal by UUID:

```bash
curl localhost:5037/animals/uid?uid='<uuid>'
```

For example:

```bash
curl localhost:5037/animals/uid?uid='84b7d90b-929d-4af7-934f-03f42e1da724'
```

Route to select animal by UUID and specify updates to its information:

```bash
curl "localhost:5037/animals/update?head='<nameofanimal>'&body='<nameofanimal>'&arms=<integernumber>&legs=<integernumber>&tails=<integernumber>&uid=<uuid>"
```

For example:

```bash
curl "localhost:5037/animals/udpate?head='snake'&body='cattle-cub'&arms=4&legs=20&tails=8&uid=84b7d90b-929d-4af7-934f-03f42e1da724"
```

Route to delete a range of animals by date:

```bash
curl "localhost:5037/animals/deletions?start='<yyyy-mm-dd_hh:mm:ss.ffffff>'&end='<yyyy-mm-dd_hh:mm:ss.ffffff>'"
```

```bash
curl "localhost:5037/animals/deletions?start='2021-04-06_02:45:29.356846'&end='2021-04-06_02:45:29.381785'"
```

Route to return the average number of legs per animal:

```bash
curl localhost:5037/animals/averagelegs
```

Route to return a total count of the animals:

```bash
curl localhost/5037:/animals/total
```

Route to reset Redis database:

```bash
curl localhost:5037/establish
```
