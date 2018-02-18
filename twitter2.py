import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'


# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py
def parser(acct):
    acct = str(acct)
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    if (len(acct) < 1): return "wrong input"
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct })
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    return js
