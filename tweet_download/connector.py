"""The module responsible for connection with a Twitter"""

import twitter

def connect(secret_one, secret_two):
    """Return Twitter API object."""

    api = twitter.Api(consumer_key='ZbrMr1Fu3T9v9jXinkHSDjFyJ',
                      consumer_secret=secret_one,
                      # not 80 lines, but who wants read it? ;)
                      access_token_key='1086897148829020160-LMjzMPIdqfZ9sHqpFOmYssvLbupGop',
                      access_token_secret=secret_two,
                      sleep_on_rate_limit=True)
    try:
        api.VerifyCredentials()
    except twitter.error.TwitterError as ex:
        print('Problem with connecting to the Twitter. Check secrets!')
        print(ex)

    return api
