#!/usr/bin/python3
'''
script to save task information for all employees in json format
'''

if __name__ == "__main__":
    import json
    import requests

    r = requests.get('https://jsonplaceholder.typicode.com/users/')
    users = r.json()

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = r.json()

    all_tasks_dict = dict()

    for employee in users:
        emp_id = employee.get('id')
        emp_name = employee.get('username')
        emp_tasks = [item for item in tasks if item.get('userId') == emp_id]

        emp_dict = {emp_id: []}
        for task in emp_tasks:
            emp_dict.get(emp_id).append({'task': task.get('title'),
                                         'completed': task.get('completed'),
                                         'username': emp_name})
        all_tasks_dict.update(emp_dict)

    with open('todo_all_employees.json', 'w+') as f:
        json.dump(all_tasks_dict, f)
