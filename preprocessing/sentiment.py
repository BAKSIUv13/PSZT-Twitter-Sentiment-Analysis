"""The module responsible for making neural network-friendly form of tweets"""

import csv
import re

def convert_tweets(tweets):
    """
    Returns the neural network-friendly form of list of tweets (array of array of double)

    tweets (array of str) – input for converter
    """
    # Stage 0: Load sentiment dictionary
    sentiment_csv = csv.reader(open("preprocessing/sentiment_dictionary_AFINN-165.csv"),
                                    delimiter="\t", doublequote=False, quoting=csv.QUOTE_NONE)
    sentiment_dict = dict(sentiment_csv)

    output_global = []

    for tweet in tweets:
        output_local = []
        # Stage 1: Split tweet into array of strings (words)
        words = tweet.split()
        

        for word in words:
            p_pos = 0.5
            p_neg = 0.5

            # Stage 2.1: Assign positivity and negativity probability as read from dictionary
            if word in sentiment_dict:
                # Word is in dictionary, so assign sentiment value to word
                word_sentiment_raw = float(sentiment_dict[word])
                p_pos = (word_sentiment_raw+5.0)/10.0
                p_neg = (10.0-(word_sentiment_raw+5.0))/10.0
            
            # Stage 2.2: Add values to tweet output array
            output_local.append(p_pos)
            output_local.append(p_neg)

        # Stage 3: Add values to (global) tweet list output array
        output_global.append(output_local)
    
    return output_global
