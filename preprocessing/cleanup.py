"""The module responsible for tweet cleanup"""

import csv
import re

def clean_tweets(tweets):
    """
    Returns the list of tidy tweets (array of str).

    tweets (array of str) – input for vaccum cleaner
    """

    output = []

    # Stage 0: Load dictionaries
    emoticons_csv = csv.reader(open("preprocessing/emoticons_dictionary.csv"),
                               delimiter=",", doublequote=False, quoting=csv.QUOTE_ALL)
    emoticons_dict = dict(emoticons_csv)
    contractions_csv = csv.reader(open("preprocessing/contractions_dictionary.csv"),
                                  delimiter=",", doublequote=False, quoting=csv.QUOTE_ALL)
    contractions_dict = dict(contractions_csv)

    for tweet in tweets:
        # Do vaccuming

        # Stage 1: Let's make everything lowercase
        tweet = tweet.lower()

        # Stage 2: Replace emoticons with text representation
        for key, value in emoticons_dict.items():
            tweet = tweet.replace(key.lower(), value.lower())

        # Stage 3: Replace contractions with full representation
        for key, value in contractions_dict.items():
            tweet = tweet.replace(key.lower(), value.lower())

        # Stage 4: Remove URL's
        tweet = re.sub(r'http\S+', '', tweet) #removes http(s) URL's
        tweet = re.sub(r'www\S+', '', tweet) #removes www URL's

        # Stage 5: Remove @at statements
        tweet = re.sub(r'rt @\S+', '', tweet) #removes http(s) URL's
        tweet = re.sub(r'@\S+', '', tweet) #removes http(s) URL's

        # Stage 6: Remove newline character and other unwanted phrases
        tweet = re.sub(r'&amp;apos;', '', tweet)
        tweet = re.sub(r'&amp;', '', tweet)
        tweet = re.sub(r'\n', '', tweet)

        # Stage 7: Remove remaining symbols and numbers => # will also be removed
        tweet = re.sub('[^A-Za-z ]+', '', tweet)

        # Stage 8: Remove trailing and duplicated spaces
        tweet = tweet.strip()
        tweet = " ".join(tweet.split())

        # Ending stage: Add modified tweet to output list
        output.append(tweet)

    return output
