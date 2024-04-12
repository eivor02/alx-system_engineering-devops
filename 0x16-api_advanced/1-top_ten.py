#!/usr/bin/python3
'''
prints top 10 hot posts in a subreddit
'''

import requests


def top_ten(subreddit):
    '''
    prints top 10 hot posts in a subreddit
    '''
    headers = {'user-agent': 'my-app/0.0.1'}

    r = requests.get('https://www.reddit.com/r/{}/hot/.json'
                     .format(subreddit),
                     headers=headers)

    try:
        for i in range(0, 10):
            print(r.json()['data']['children'][i]['data']['title'])
    except (KeyError, IndexError):
        print('None')
