from collections import namedtuple
from pprint import pprint

Cricketer = namedtuple('Cricketer', [
    'name',
    'age',
    'matches'
])

c1 = Cricketer(name='sachin', age=40, matches=400)
c2 = Cricketer(name='sunil', age=60, matches=300)
c3 = Cricketer(name='kapil', age=55, matches=330)

# -- can access properties
# print(c1.name)
# -- can't modify
# c1.name = 'someguy'

my_fav_list = (c1, c2, c3)
pprint(my_fav_list)
print(f"Count of players: {len(my_fav_list)}")

# Apply a filter on my_fav_list to return cricketers who has played exactly 300 matches
my_filter = filter(lambda c: c.matches == 300, my_fav_list)
# convert filter object into a tuple
pprint(tuple(my_filter))

# you can use list comprehension to generate a list (mutable)
# my_list = [x for x in my_fav_list if x.name != 'anil']
# pprint(my_list)
