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


def dictionary_of_list_of_dictionaries():
    """
    Fetches and displays the progress of an employee's TODO list.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = f"https://jsonplaceholder.typicode.com/users"
    response = requests.get(base_url)
    user_data = response.json()
    output_dic = {}
    for user in user_data:
        employee_id = user['id']
        USERNAME = user['username']
        todo_url = (
                f"https://jsonplaceholder.typicode.com/todos"
                f"?userId={employee_id}"
                )
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        output = []
        for task in todo_data:
            dic = {}
            dic["username"] = USERNAME
            dic["task"] = task['title']
            dic["completed"] = task['completed']
            output.append(dic)

        output_dic[employee_id] = output

    outputjson = json.dumps(output_dic)
    with open(f"todo_all_employees.json", 'w') as f:
        f.write(outputjson)


if __name__ == "__main__":
    dictionary_of_list_of_dictionaries()
