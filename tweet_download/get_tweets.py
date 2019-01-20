"""The module responsible for getting tweets."""

from tweet_download import connector

class Tweets:
    """The module responsible for getting tweets."""

    def __init__(self, secret_one, secret_two):
        self._con = connector.connect(secret_one, secret_two)

    def get_tweets(self, hashtag, tweet_counter=15, tweets_type='mixed'):
        """
        Returns the list of tweets.

        tweets_type (str, optional) – Type of result which should be returned.
        Default is “mixed”. Valid options are “mixed, “recent”, and “popular”.
        """

        tweets = self._con.GetSearch(term='#' + hashtag,
                                     count=tweet_counter,
                                     lang='en',
                                     result_type=tweets_type)
        tweet_list = [tweet.text for tweet in tweets]

        return tweet_list

    def get_api(self):
        """Return copy of api connection"""

        return self._con
