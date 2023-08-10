#!/usr/bin/python3
"""
Python script that takes in a letter and sends a 
POST request to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

def main():
    """
    Sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter,
    and processes the JSON response.

    Usage:
        python script.py <letter>

    Args:
        <letter>: The letter to be used as a parameter in the POST request. Optional.

    Returns:
        None
    """

    # Check if a letter argument is provided, otherwise set q=""
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    # Prepare the data to be sent in the POST request
    data = {'q': letter}

    try:
        # Send a POST request to the specified URL with the letter data
        response = requests.post('http://0.0.0.0:5000/search_user', data=data)

        # Parse the JSON response
        try:
            json_response = response.json()
            if isinstance(json_response, dict) and 'id' in json_response and 'name' in json_response:
                print("[{}] {}".format(json_response['id'], json_response['name']))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

if __name__ == "__main__":
    main()

