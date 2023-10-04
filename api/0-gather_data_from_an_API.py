#!/usr/bin/python
"""
This is a python script that, uses REST API
for a given employee ID, returns information about his/her TODO list progress.
"""
import requests

def getEmployeeTodoProgress(employee_id):
    # Fetching employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found.")
        return

    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetching TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error: Failed to fetch TODO list for employee with ID {employee_id}.")
        return

    todos_data = todos_response.json()

    # Calculating TODO list progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])
    completed_task_titles = [todo['title'] for todo in todos_data if todo['completed']]

    # Displaying the progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for task_title in completed_task_titles:
        print(f"\t{task_title}")

if __name__ == "__main__":
    employee_id = int(input("Enter Employee ID: "))
    getEmployeeTodoProgress(employee_id)
