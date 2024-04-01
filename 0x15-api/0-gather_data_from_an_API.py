#!/usr/bin/python3
'''
script to get information on an employee's tasks
'''

if __name__ == "__main__":
    import requests
    from sys import argv

    emp_id = int(argv[1])
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(emp_id))
    emp_name = r.json().get('name')

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = r.json()
    all_tasks = [item for item in tasks if item.get('userId') == emp_id]
    done_tasks = [item for item in all_tasks if item.get('completed') is True]

    print('Employee {} is done with tasks({}/{}):'.format(emp_name,
                                                          len(done_tasks),
                                                          len(all_tasks)))
    for task in done_tasks:
        print('\t {}'.format(task.get('title')))
