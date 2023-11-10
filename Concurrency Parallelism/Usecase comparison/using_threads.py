from threading import Thread, current_thread
import os
import requests
import json
import time

"""
Python's standard implementation of threading limits threads to only being able to execute one at a time due to 
something called the Global Interpreter Lock (GIL). The GIL is necessary because CPython's (Python's default implementation) 
memory management is not thread-safe. Because of this limitation, threading in Python is concurrent, but not parallel. 
To get around this, Python has a separate multiprocessing module not limited by the GIL that spins up separate processes, 
enabling parallel execution of your code. Using the multiprocessing module is nearly identical to using the threading module.
"""
def write_genre(filename):
    """
    Get a random genre using REST endpoint
    """
    t_name = current_thread().getName()
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
    # skip ssl verification
    # r = requests.get(url, headers=headers, verify=False)
    r = requests.get(url, headers=headers)
    resp_code = r.status_code
    # response = json.loads(r.text)
    # print(f"Code: {resp_code} Msg: {response}")

    with open(filename, "w") as fh:
        # print(f"{t_name} writing genre {response} to {filename}")
        print(f"{t_name} writing genre {r.text} to {filename}")
        fh.write(r.text)

# file = "genre.txt"
# write_genre(file)
start_time = time.time()
threads = []

for i in range(5):
    filename = f"genre-{i}.txt"
    t = Thread(name=f"T-{i}", target=write_genre, args=(filename,))
    threads.append(t)
    t.start()

# wait for threads to complete
for t in threads:
    t.join()
end_time = time.time()

print(f"Execution took {(end_time - start_time)} secs")