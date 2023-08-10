#!/usr/bin/python3
"""
This module sends request to the server and gets a feedback 
Using the import  to import the requests package.
"""
import requests
#url to fetch the data from the intranet

url = "https://alu-intranet.hbtn.io/status"


#using Get method to send a get request to server
response = requests.get(url)

"""
    using if statement to check if data is in json format
    and checking if the status code is ok
"""
if response.status_code ==  200:
    #checks if the data is in Json format
    data = response.json()
    print("Body response:")
    print("\t - type:", type(data))
    print("\t - content:",data)
