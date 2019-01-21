#!PSZT-Twitter-Sentiment-Analysis-env/bin/python3
"""This is the main module in the PSZT-Twitter-Sentiment-Analysis"""

import sys

from user_interface import main_user_interface

SECRET_ONE = sys.argv[2]
SECRET_TWO = sys.argv[3]

(main_user_interface.MainUserInterface(SECRET_ONE, SECRET_TWO)
 .check_hashtag(sys.argv[1]))
