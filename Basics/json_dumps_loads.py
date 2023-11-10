import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
print("x type: ")
print(type(x))

# convert python object into JSON string:
y = json.dumps(x)

# the result is a JSON string:
print("y type: ")
print(type(y))

# some JSON:
x2 = '{ "name":"John", "age":30, "city":"New York"}'
print("x2 type: ")
print(type(x2))

# convert JSON string into python object
y2 = json.loads(x2)
print("y2 type: ")
print(type(y2))

# the result is a Python dictionary:
print("Age: ")
print(y2["age"])

