#!/usr/bin/python3
'''
script to save task information in csv format
'''

if __name__ == "__main__":

    import requests
    from sys import argv

    emp_id = int(argv[1])
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(emp_id))
    emp_name = r.json().get('username')

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = r.json()
    all_tasks = [item for item in tasks if item.get('userId') == emp_id]

    with open('{}.csv'.format(emp_id), 'w+') as f:
        for item in all_tasks:
            f.write('"{}","{}","{}","{}"\n'.format(emp_id, emp_name,
                                                   item.get('completed'),
                                                   item.get('title')))
