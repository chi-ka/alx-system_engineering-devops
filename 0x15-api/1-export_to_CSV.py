#!/usr/bin/python3

"""
Fetches and displays the progress of an employee's TODO list.

Args:
    employee_id (int): The ID of the employee.

Returns
None
"""

import requests
import sys


def export_to_CSV(employee_id):
    """
    Fetches and displays the progress of an employee's TODO list.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = (
            f"https://jsonplaceholder.typicode.com/users/{employee_id}"
            )
    response = requests.get(base_url)
    user_data = response.json()
    USERNAME = user_data['username']
    if 'id' not in user_data:
        print("Employee not found.")
        return

    todo_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
            )
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    with open(f'{employee_id}.csv', "w") as f:
        for task in todo_data:
            id = employee_id
            f.write(
                    f"{id}, {USERNAME}, {task['completed']}, {task['title']}\n"
                    )

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_CSV(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
