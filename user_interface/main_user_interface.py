"""The module responsible for user interface."""

from tweet_download import get_tweets
from preprocessing import cleanup
from preprocessing import sentiment
import network_manager

class MainUserInterface:
    """The class responsible for user interface."""

    def __init__(self, secret_one, secret_two):
        # TODO
        self._neural_network = network_manager.create_zero_network()
        self._secret_one = secret_one
        self._secret_two = secret_two

    def check_hashtag(self, hashtag, number_of_tweets, tweets_type):
        """Check sentiment."""

        tweets = (get_tweets.Tweets(self._secret_one, self._secret_two)
                  .get_tweets(hashtag,
                              number_of_tweets,
                              tweets_type))

        for tweet in tweets:
            print(tweet)
            print()
            print()
        clean_tweets = cleanup.clean_tweets(tweets)
        sentimated_tweets = sentiment.convert_tweets(clean_tweets)

        positives = []
        negatives = []

        for sentimated_tweet in sentimated_tweets:
            partial_result = (self._neural_network
                              .get_calculation(sentimated_tweet))
            positives.append(partial_result[0])
            negatives.append(partial_result[1])

        average_positive = sum(positives) / len(positives)
        average_negative = sum(negatives) / len(negatives)

        print(f'Positive: {average_positive}%')
        print(f'Negative: {average_negative}%')
