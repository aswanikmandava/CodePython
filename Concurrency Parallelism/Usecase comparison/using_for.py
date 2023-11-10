import os
import requests
import json
import time


def write_genre(filename):
    """
    Get a random genre using REST endpoint
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
    # skip ssl verification
    # r = requests.get(url, headers=headers, verify=False)
    r = requests.get(url, headers=headers)
    # print(f"response encoding type: {r.encoding} headers: {r.headers}")
    # resp_code = r.status_code
    response = json.loads(r.text)
    # print(f"Code: {resp_code} Msg: {response}")

    with open(filename, "w") as fh:
        print(f"writing genre {response} to {filename}")
        fh.write(response)

start_time = time.time()
pid = os.getpid()
for i in range(5):
    filename = f"genre-{i}.txt"
    write_genre(filename)

end_time = time.time()

print(f"{pid} Execution took {(end_time - start_time)} secs")