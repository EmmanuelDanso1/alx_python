#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to 
the URL and displays the value of the variable X-Request-Id
in the response header
Takes two import packages
"""
import requests
import sys

def main():
    """
    Fetches a URL and displays the value of the X-Request-Id variable in the response header.
    Usage:
        python script.py <URL>
    Args:
        None (Uses sys.argv to retrieve the URL from the command-line argument)
    Returns:
        None
    """

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        return

    # Retrieve the URL from the command-line argument
    url = sys.argv[1]
    #  try:
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Retrieve the value of the X-Request-Id header from the response
        x_request_id = response.headers.get('X-Request-Id')
        
        # Check if X-Request-Id header exists in the response
        if x_request_id:
                print("X-Request-Id:", x_request_id)
        else:
                print("X-Request-Id not found")
    else:
        print("Error:", response.status_code)
    #except (requests.exceptions.RequestException, requests.exceptions.ConnectionError, requests.exceptions.MaxRetryError) as e:
        #print("Request Error:", e)

if __name__ == "__main__":
    main()