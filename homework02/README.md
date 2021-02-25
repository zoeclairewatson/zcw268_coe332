
# Homework 2: The Containers and Repositories of Dr. Moreau

The purpose of this project is to build upon homework 1, where one script generated a JSON file of assembled animals and another one that read in and printed one animal at random. Here, the scipt to read in and print has been expanded to include a new breeding feature, a unit test has been included to test this new feature, and a Dockerfile has been written to containerize both scripts.

## Installation

Install this project by cloning the repository, making the scripts executable, and adding them to your PATH. For example:

```bash
git clone https://github.com/zoeclairewatson/zcw268_coe332.git
chmod +rx generate_animals.py
chmod +rx read_animals.py
export PATH=/code:$PATH
```

## Running the Code

This code has two functions: to generate a JSON file of assembled animals and to read in this file for printing.

To generate JSON file:

```bash
generate_animals.py animals.json
```

To read in JSON file and print animals to screen:

```bash
read_animals.py animals.json
```

## Docker Image

You can build a Docker image using the provided Dockerfile. Use the commands:

```bash
git clone https://github.com/zoeclairewatson/zcw268_coe332.git
cd repo/
docker build -t zoeclairewatson/bizarre-animals:1.1 .
```

An example of running the scripts inside a container is:

```bash
docker run --rm -v $PWD:/data zoeclairewatson/bizarre-animals:1.1 generate_animals.py /data/animals.json

docker run --rm -v $PWD:/data zoeclairewatson/bizarre-animals:1.1 read_animals.py /data/animals.json
```

## Test

Test
