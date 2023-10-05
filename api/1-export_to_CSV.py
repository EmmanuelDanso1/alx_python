#!/usr/bin/python
"""

Python script to export data in the CSV format
"""

import csv
import requests
import sys

def get_employee_todo_list(employee_id):
    # Defining the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetching employee details
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)

    # Checking if the employee exists
    if employee_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return

    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    # Fetching employee's TODO list
    todo_url = f"{base_url}/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)

    if todo_response.status_code != 200:
        print(f"Failed to retrieve TODO list for Employee {employee_name}.")
        return

    todo_list = todo_response.json()

    # Creating a CSV file for the employee's TODO list
    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Writing CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        # Writing TODO list data to CSV
        for task in todo_list:
            csv_writer.writerow([employee_id, employee_name, task["completed"], task["title"]])

    print(f"CSV file '{csv_filename}' created with TODO list for Employee {employee_name}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_list(employee_id)
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
