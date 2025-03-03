import sys
from gemini import prompt

tweet = sys.argv[1]
tweet_en = prompt(tweet)

with open(f'/tmp/tweet-en.txt', "w") as f:
    f.write(tweet_en.replace('"', ''))