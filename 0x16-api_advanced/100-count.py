#!/usr/bin/python3
'''
prints keyword count for titles of hot posts in a subreddit
'''

import requests


def count_words(subreddit, word_list, after='', keywords=None):
    '''
    prints keyword count for titles of hot posts in a subreddit
    '''
    headers = {'user-agent': 'my-app/0.0.1'}

    r = requests.get('https://www.reddit.com/r/{}/hot/.json?after={}'
                     .format(subreddit, after),
                     headers=headers)

    if keywords is None:
        keywords = {key: 0 for key in word_list}

    try:
        if r.json()['data']['dist'] == 0:
            return None
        for post in r.json()['data']['children']:
            title = post['data']['title'].lower()
            for word in word_list:
                keywords[word] += title.count(word)
    except (KeyError, IndexError):
        if after == '':
            return None

    if (r.json()['data']['after'] is None):
        return keywords

    keywords = count_words(subreddit, word_list,
                           r.json()['data']['after'], keywords)

    if after == '':
        for key, value in sorted(keywords.items(),
                                 key=lambda tup: tup[1], reverse=True):
            if (value != 0):
                print('{}: {}'.format(key, value))

    return(keywords)
