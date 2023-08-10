#!/usr/bin/python3
"""
This module sends request to the server and gets a feedback 
By using thr import module to request data.
"""
import requests
"""
url to fetch the data from
"""
url = "https://alu-intranet.hbtn.io/status"

"""
using get method to fetch response  from server
"""
response = requests.get(url)
"""
using if statement to check if data is in json format
"""
if response.status_code ==  200:
    data = response.json()
