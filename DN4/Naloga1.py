import json

#Python:
podatki = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

#pretvorba v JSON:
y = json.dumps(podatki)
print(y)