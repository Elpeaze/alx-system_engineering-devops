#!/usr/bin/python3
"""
This script returns information about an employee's TODO list progress,
using this REST API.
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])
    user_endp = "{}/users/{}".format(url, user_id)
    name = requests.get(user_endp).json().get("name")
    tasks_endp = "{}/todos".format(url)
    tasks = requests.get(tasks_endp).json()
    tasks_user = [task for task in tasks if task.get("userId") == user_id]
    tasks_completed = [task for task in tasks_user if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(tasks_completed), len(tasks_user)))

    for task in tasks_completed:
        print("\t{}".format(task.get("title")))
