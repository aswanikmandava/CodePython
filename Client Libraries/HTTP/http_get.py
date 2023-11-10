import requests
from requests.auth import HTTPBasicAuth


# make a HTTP GET request to the web server
site_url = "https://www.geeksforgeeks.org/python-requests-tutorial/#"
res = requests.get(url=site_url, auth=HTTPBasicAuth('user', 'pwd'), verify=False)

# response object
print(res)

# get HTTP response code
print(res.status_code)

# get HTTP response content in bytes
print(res.content)