#!/usr/bin/python3

"""
Fetches and displays the progress of an employee's TODO list.

Args:
    employee_id (int): The ID of the employee.

Returns
None
"""

import json
import requests
import sys


def export_to_json(employee_id):
    """
    Fetches and displays the progress of an employee's TODO list.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
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

    output = []
    for task in todo_data:
        dic = {}
        dic["task"] = task['title']
        dic["completed"] = task['completed']
        dic["username"] = USERNAME
        output.append(dic)

    output_dic = {}
    output_dic[employee_id] = output

    outputjson = json.dumps(output_dic)

    with open(f"{employee_id}.json", 'w') as f:
        f.write(outputjson)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
