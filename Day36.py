""" Request Module in Python"""
import json

""" The Python Requests module in an HTTP library that enables
    developers to send HTTP requests in python. This module enables you
    to send HTTP requests using Python code and makes its possible to interact with APIs and web services"""

""" Installation """
""" pip install requests """

""" Get Requests """
""" Once you have installed the requests module, you can start using it ti send HTTP requests.
    Here is a single example that sends a GET requests to the google homepage: """

import requests
from bs4 import BeautifulSoup
# response = requests.get('https://google.com')
# print(response.text)

url = "https://luciferdonghua.in/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

# data = {
#     "name" : "Himal",
#     "caste" : "Rajbanshi",
#     "userid" : 101
# }
# headers = {"Content-Type": "application/json;charset=utf-8"}
# response = requests.post(url, data=json.dumps(data), headers=headers)
# print(response.json())