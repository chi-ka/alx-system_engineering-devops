#!/usr/bin/python3

import sys
import requests


def fetch_todo_progress(employee_id):
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

    if user_data.get("id") is None:
        print("Employee not found.")
        return

    todo_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    completed_tasks = [
        task["title"] for task in todo_data if task.get("completed")
    ]
    total_tasks = len(todo_data)
    completed_count = len(completed_tasks)

    print(
        f"Employee {user_data.get('name')} is done with tasks "
        f"({completed_count}/{total_tasks}):"
    )
    for task_title in completed_tasks:
        print(f"\t{task_title}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
