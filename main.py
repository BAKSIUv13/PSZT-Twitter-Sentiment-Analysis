"""This is the main module in the PSZT-Twitter-Sentiment-Analysis"""

from tweet_download import get_tweets
from preprocessing import cleanup
from preprocessing import sentiment
from preprocessing import sentiment

from afinn import Afinn
from sets import sets

sets.make_set(['USA', 'giveaway', 'win', 'photography', 'happybirthday', \
                'movies', 'medicare', 'bitcoin', 'crypto', 'happy', 'sad', \
                 'failure', 'influencermarketing', 'healthinsurance', 'unhappy'], "training", \
                 '1v6hhGfhQlk35JzkcdskAHS9dHe126I9R8o1089vuPLwjTOfiU', \
                 'mwFen4DQmTN8DQC0YOqD9qCu8FhVDQ2YEbxGqRTxbgY6B')


sets.make_set(['Poland', 'happyeaster', 'olympics', 'cryptocurrency'], "test", \
                 '1v6hhGfhQlk35JzkcdskAHS9dHe126I9R8o1089vuPLwjTOfiU', \
                 'mwFen4DQmTN8DQC0YOqD9qCu8FhVDQ2YEbxGqRTxbgY6B')