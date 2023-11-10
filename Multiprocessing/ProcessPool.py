from collections import namedtuple
import concurrent.futures
import os
import time
from pprint import pprint

Cricketer = namedtuple('Cricketer', ['name', 'age', 'matches'])

player = (
    Cricketer(name='Sachin', age=45, matches=400),
    Cricketer(name='Sunil', age=60, matches=300),
    Cricketer(name='Azhar', age=50, matches=250)
)
# pprint(player)

def transform(item):
    print(f"PID: {os.getpid()} - processing {item.name}")
    time.sleep(1)
    result = {'name': item.name, 'age': item.age, 'dob': 2021 - item.age}
    print(f"PID: {os.getpid()} - DONE processing {item.name}")
    return result

start_time = time.time()

try:
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = pool.map(transform, player)
except Exception as e:
    print(f"{e}")

end_time = time.time()
print(f"time to complete - {end_time - start_time:.2f}s")
print(tuple(result))