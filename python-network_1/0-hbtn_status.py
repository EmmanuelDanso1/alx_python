#!/usr/bin/python3
"""
Module to fetch and display the status https://alu-intranet.hbtn.io/status
"""
import requests

#url to fetch the data from the intranet
url = "https://alu-intranet.hbtn.io/status"

#sends GET request to the url
response = requests.get(url)

#checks if the response status code is 200
if response.status_code ==  200:
        print("Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)
