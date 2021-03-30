import requests

response = requests.get(url="http://localhost:5037/animals")
response = requests.get(url="http://localhost:5037/animals/head?head='bunny'")
response = requests.get(url="http://localhost:5037/animals/legs?num_legs=6")


#let's look at the response code
print(response.status_code)
print(response.json())
print(response.headers)
