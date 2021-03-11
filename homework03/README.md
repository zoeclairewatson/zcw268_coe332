
# Homework 3: Containerizing Flask

The purpose of this project is to build upon homework 2, where one script generated a JSON file of assembled animals and another one that read in and printed one animal at random, as well as incorporating a new breeding feature. Here, a Flask app (app.py is the python script) has been created to access the generated JSON file of animals(animals_data.json), including routes to access specific data relating to the animals within the file. A Dockerfile has been written to containerize the Flask app, and a consumer file has been written for peers to consume this data.

##Installation

Install this project by cloning the repository, then navigating to the web directory within the homework03 directory. For example:

```bash
git clone https://github.com/zoeclairewatson/zcw268_coe332.git
cd homework03
cd web
```

##Running the Code

This directory already has the JSON file of assembled animals included.

##Docker Image

You can build a Docker image using the provided Dockerfile within this web directory. Use the command:

```bash
docker build -t flask-animals-watson:latest .
```

To run the container:

```bash
docker run --name "zoe-animals" -d -p 5037:5000 flask-animals-watson
```

##Curl the Port

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

##Consumer File

This file provides URLs for others to consume this data.
