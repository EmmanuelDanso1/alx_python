#!/usr/bin/python
"""
This is a python script that, uses REST API
for a given employee ID, returns information about his/her TODO list progress.
"""
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

    # Calculating the number of completed tasks
    completed_tasks = [task for task in todo_list if task["completed"]]
    total_tasks = len(todo_list)
    completed_count = len(completed_tasks)

    # Displaying the progress
    print(f"Employee {employee_name} is done with tasks ({completed_count}/{total_tasks}):")

    # Displaying completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_list(employee_id)
    except ValueError:
        print("Please provide a valid integer for the employee ID.")

