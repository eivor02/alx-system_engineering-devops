#!/usr/bin/python3
'''
script to save task information in json format
'''

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    emp_id = argv[1]
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(emp_id))
    emp_name = r.json().get('username')

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = r.json()
    all_tasks = [item for item in tasks if item.get('userId') == int(emp_id)]

    emp_dict = {emp_id: []}
    for task in all_tasks:
        emp_dict.get(emp_id).append({'task': task.get('title'),
                                     'completed': task.get('completed'),
                                     'username': emp_name})

    with open('{}.json'.format(emp_id), 'w+') as f:
        json.dump(emp_dict, f)
