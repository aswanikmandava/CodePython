months = {"0": "Jan", "1": "Feb", "2": "March"}

# keys
print("Return type: ", type(months.keys()))
print("Keys:", months.keys())

# values
print("Values:", months.values())

# items
print("Return type:", type(months.items()))
print("Items:", months.items())

# Iterate through items and print key and value
for key, value in months.items():
    print("Key:", key, "Value:", value)

# Iterate through keys
for key in months.keys():
    print("Key:", key)

# Iterate through values
for value in months.values():
    print("Value:", value)

# update method
response = {'cm': {'cmk': 'cmv'}, 'cmts': {'cmtsk':'cmtsv'}}
cm_result = {'data': {'.1.2.3.4':0.0, '2.3.3.4': 1.1, 'cmk2': 'cmv2'}}

# print(cm_result['data'])
# updates a dictionary with key/value pair from the input dictionary
# if a key already exists - its value is updated with the one from the input argument
# if it doesn't - adds a new key/value pair
response['cm'].update(cm_result['data'])

print(response)