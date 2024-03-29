#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        print('Employee ID is required')
    else:
        user_url = 'https://jsonplaceholder.typicode.com/users/{}'\
                   .format(argv[1])
        response = requests.get(user_url)

        try:
            completed_count = 0
            if response.status_code == 200:
                user = response.json()
                todo_url = 'https://jsonplaceholder.typicode.com/todos'

                res = requests.get(todo_url)
                todos = res.json()
                user_todos = []

                for todo in todos:
                    if todo.get('userId') == user.get('id'):
                        user_todos.append(todo)

                completed = ''
                for todo in user_todos:
                    if todo.get('completed'):
                        completed_count += 1
                        completed += "\n\t {}".format(todo.get('title'))

                result = "Employee {} is done with tasks({}/{}):"\
                         .format(user.get('name'), completed_count,
                                 len(user_todos), completed)
                print("{}{}".format(result, completed))
            else:
                raise Exception("Error: {}".format(response.status_code))
        except Exception as e:
            print(e)
