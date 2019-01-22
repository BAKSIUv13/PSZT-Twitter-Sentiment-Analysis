# PSZT-Twitter-Sentiment-Analysis

## Setting up environment

To create python virtual environment:

`python3 -m venv PSZT-Twitter-Sentiment-Analysis-env`

To activate PSZT-Twitter-Sentiment-Analysis-env:

`source PSZT-Twitter-Sentiment-Analysis-env/bin/activate`

To install requirements:

`pip install -r requirements.txt`

## Running the program

To run the program:

`./main.py <HASHTAG> <NUMBER_OF_TWEETS> <TWEETS_TYPE> <SECRET_ONE> <SECRET_TWO>`

`<TWEETS_TYPE>` - mixed, recent or popular

- mixed : Include both popular and real time results in the response

- recent : return only the most recent results in the response

- popular : return only the most popular results in the response

All arguments are required.

For example:

`./main.py trump 15 mixed SECRET_ONE SECRET_TWO`
