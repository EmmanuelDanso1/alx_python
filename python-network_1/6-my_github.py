#!/usr/bin/python3
"""
Python script that takes your
GitHub credentials (username and password) and 
uses the GitHub API to display your id
"""
import requests
import sys

def main():
    """
    Uses Basic Authentication with a personal access token to access the GitHub API
    and display the GitHub user ID.

    Usage:
        python script.py <username> <personal_access_token>

    Args:
        <username>: Your GitHub username.
        <personal_access_token>: Your GitHub personal access token.

    Returns:
        None
    """

    # Retrieve GitHub username and personal access token from command-line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # Create the Basic Authentication header using the personal access token
    auth = (username, token)

    try:
        # Send a GET request to the GitHub API to retrieve user information
        response = requests.get('https://api.github.com/user', auth=auth)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            user_info = response.json()
            user_id = user_info['id']
            print(user_id)
        else:
            print("Error:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

if __name__ == "__main__":
    main()
