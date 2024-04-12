#!/usr/bin/python3
'''
returns number of subscribers for a given subreddit
'''

import requests


def number_of_subscribers(subreddit):
    '''
    returns number of subscribers for a given subreddit
    '''
    headers = {'user-agent': 'my-app/0.0.1'}

    r = requests.get('https://www.reddit.com/r/{}/about/.json'
                     .format(subreddit),
                     headers=headers)

    try:
        return r.json()['data']['subscribers']
    except KeyError:
        return 0
