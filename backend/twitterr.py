from TwitterAPI import TwitterAPI

import config


def hasher(hashtag):
    api = TwitterAPI(config.consumer_key, config.consumer_secret, config.access_token_key, config.access_token_secret)
    twitterDict = []
    r = api.request('search/tweets', {'q': '#{}'.format(hashtag)})
    for item in r:
        twitterDict.append(item['user']['profile_image_url']+"||"+item['text'])

    return twitterDict


