"""This is the main module in the PSZT-Twitter-Sentiment-Analysis"""

from tweet_download import get_tweets
from preprocessing import cleanup
from preprocessing import sentiment

from afinn import Afinn

def make_set(list_of_tags, set_name, secret1, secret2):
    #Stage 1: Connect and download Tweets using tweet_download module
    TWEET_MANAGER = get_tweets.Tweets(secret1,
                                    secret2)

    TWEETS = []
    for tag in list_of_tags:
        TWEETS += TWEET_MANAGER.get_tweets(tag, tweet_counter=100)



    #TWEETS = ["I'm a very smart person | :) :( xD =^.^= http://lol.pl https://lol2.pl www.lol3.pl",
    #          "RT @kot1 rt at test", "blah @kot2 at test", " no \n\n\n newlines nor        duplicated spaces", " no symb$$ols and num123bers"]

    #TWEETS = ["Sacha is the best tutor."]
    #print("Before:")
    #print(TWEETS)
    f = open(set_name + '_tweets_beforeparsing.py', 'wb')
    f.write((set_name + '_tweets_beforeparsing = ' + repr(TWEETS) + '\n').encode('utf8'))
    f.close

    afinn = Afinn()

    # TRAINING SET
    # STAGE1 - call afinn to calculate scores
    training_scores = []
    min_score = 10000
    max_score = -10000
    for tweet in TWEETS:
        score = afinn.score(tweet)
        if score < min_score:
            min_score = score
        if score > max_score:
            max_score = score
        outArray = []
        outArray.append(score)
        outArray.append(score)
        training_scores.append(outArray)
    #STAGE2 - scale scores to be compatible with our neural network
    for scorepair in training_scores:
        score = scorepair[0]
        p_pos = 0
        p_neg = 0
        if score >= 0:
            score = score / max_score
            p_pos = (score+1.0)/2.0
            p_neg = (2.0-(score+1.0))/2.0
        if score < 0:
            score = -score
            score = score / (-min_score)
            p_neg = (score+1.0)/2.0
            p_pos = (2.0-(score+1.0))/2.0
        scorepair[0] = p_pos
        scorepair[1] = p_neg


    #print("AFINN scores:")
    #print(training_scores)
    f = open(set_name + '_scores.py', 'w')
    f.write(set_name + '_scores = ' + repr(training_scores) + '\n')
    f.close


    TIDIED_TWEETS = cleanup.clean_tweets(TWEETS)

    #print("After:")
    #print(TIDIED_TWEETS)
    f = open(set_name + '_tweets_afterparsing.py', 'wb')
    f.write((set_name + '_tweets_afterparsing = ' + repr(TIDIED_TWEETS) + '\n').encode('utf8'))
    f.close

    SENTIMENTED_TWEETS = sentiment.convert_tweets(TIDIED_TWEETS)

    #print("Sentiment:")
    #print(SENTIMENTED_TWEETS)
    f = open(set_name + '_input.py', 'w')
    f.write(set_name + '_input = ' + repr(SENTIMENTED_TWEETS) + '\n')
    f.close

    print("\n\n" + set_name + " Tweets done: " + str(len(TWEETS)))
    print("" + set_name + " scores done: " + str(len(training_scores)))
    print("" + set_name + " inputs done: " + str(len(SENTIMENTED_TWEETS)))
