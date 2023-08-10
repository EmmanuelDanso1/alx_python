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
    Sends a POST request with an email parameter to a specified URL and displays the response body.

    Usage:
        python script.py <URL> <email>

    Args:
        None
         (Uses sys.argv to retrieve the URL and email from the command-line arguments)

    Returns:
        None
    """

    # Checks if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        return

    # Retrieves the URL and email from the command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to be sent in the POST request
    data = {'email': email}

    try:
        # Send a POST request to the specified URL with the email data
        response = requests.post(url, data=data)

        # Display the body of the response
        print("Response body:")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

if __name__ == "__main__":
    main()
