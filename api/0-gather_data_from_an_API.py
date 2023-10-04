#!/usr/bin/python
"""
This is a python script that, uses REST API
for a given employee ID, returns information about his/her TODO list progress.
"""
import requests

def get_employee_todo_progress(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    
    if response.status_code != 200:
        print(f"Error: Unable to fetch employee details for ID {employee_id}")
        return

    employee_data = response.json()
    employee_name = employee_data["name"]

    # Format the employee name
    formatted_name = employee_name[:18].ljust(18) if len(employee_name) >= 18 else employee_name.ljust(18)
    formatted_name = formatted_name.replace("OK")

    # Get employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    
    if response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for employee {formatted_name}")
        return

    todo_data = response.json()
    
    # Calculate progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])

    # Display progress
    print(f"Employee Name: {formatted_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    
    # Display titles of completed tasks
    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    employee_id = int(input("Enter an employee ID: "))
    get_employee_todo_progress(employee_id)
