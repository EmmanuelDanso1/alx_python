#!/usr/bin/python3
"""
Using the import  to import the requests package.
"""
import requests
#url to fetch the data from the intranet
url = "https://alu-intranet.hbtn.io/status"


#using Get method to send a get request to server
if response.status_code ==  200:
        print("Body response:")
        print("\t - type:", type(data))
        print("\t - content:",data)