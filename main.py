#!PSZT-Twitter-Sentiment-Analysis-env/bin/python3
"""This is the main module in the PSZT-Twitter-Sentiment-Analysis"""

import sys

from user_interface import main_user_interface

HASHTAG = sys.argv[1]
NUMBER_OF_TWEETS = sys.argv[2]
TWEETS_TYPE = sys.argv[3]

SECRET_ONE = sys.argv[4]
SECRET_TWO = sys.argv[5]

(main_user_interface.MainUserInterface(SECRET_ONE, SECRET_TWO)
 .check_hashtag(HASHTAG, NUMBER_OF_TWEETS, TWEETS_TYPE))
