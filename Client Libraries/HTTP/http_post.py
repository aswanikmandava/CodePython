import requests
from requests.auth import HTTPBasicAuth
import json

Response = requests.post(url="https://www.google.com/",
                            data="dummy data",
                            headers={"Content-Type": "application/json"},
                            auth=HTTPBasicAuth('user', 'pwd'),
                            verify=False)