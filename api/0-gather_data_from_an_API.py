#!/usr/bin/python3
""" ToDo list"""
import requests
import sys

if __name__ == "__main__":
    employee_url = "https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = "https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    employee_id = int(sys.argv[1])

    employee_data = requests.get(employee_url.format(employee_id=employee_id)).json()
    employee_name = employee_data['name']

    todo_data = requests.get(todo_url.format(employee_id=employee_id)).json()

    num_completed_tasks = 0
    for task in todo_data:
        if task['completed']:
            num_completed_tasks += 1

    total_num_tasks = len(todo_data)
    print(f"Employee {employee_name} is done with tasks \
          ({num_completed_tasks}/{total_num_tasks}):")

    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")
