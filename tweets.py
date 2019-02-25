from bs4 import BeautifulSoup as bs
import requests
from random import choice

def get_tweet(username):
    url = "https://www.twitter.com/"+username
    try:
        res = requests.get(url)
        soup = bs(res.content, 'html.parser')
        soup = soup.find_all('p', {'class': 'tweet-text'})
        tweets = []
        for tweet in soup:
            tweets.append(tweet.text)
        return tweets
    except:
        print("very sorry something went wrong")

