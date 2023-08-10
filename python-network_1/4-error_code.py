#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the variable
X-Request-Id in the response header
"""
import requests
import sys

def main():
    """
    Sends a GET request with an email parameter to a specified URL and displays the response body.

    Usage:
        python script.py <URL>

    Args:
        None
         (Uses sys.argv to retrieve the URL from the command-line arguments)

    Returns:
        None
    """
    # Retrieve the URL from the command-line argument
    url = sys.argv[1]

    #try:
        # Send a GET request to the specified URL
    response = requests.get(url)

        # Display the body of the response
    print(response.text)

        # Check if the response status code is greater than or equal to 400
    if response.status_code >= 400:
            print("Error code:", response.status_code)

    #except requests.exceptions.RequestException as e:
        #print("Request Error:", e)

if __name__ == "__main__":
    main()
