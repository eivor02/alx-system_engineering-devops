#!/usr/bin/python3
'''
returns full list of hot posts in a subreddit
'''

import requests


def recurse(subreddit, hot_list=[], after=''):
    '''
    returns full list of hot posts in a subreddit
    '''
    headers = {'user-agent': 'my-app/0.0.1'}

    r = requests.get('https://www.reddit.com/r/{}/hot/.json?after={}'
                     .format(subreddit, after),
                     headers=headers)

    try:
        if r.json()['data']['dist'] == 0:
            return None
        for post in r.json()['data']['children']:
            hot_list.append(post['data']['title'])
    except (KeyError, IndexError):
        if (after == ''):
            return None

    if (r.json()['data']['after'] is None):
        return hot_list

    return recurse(subreddit, hot_list, r.json()['data']['after'])
