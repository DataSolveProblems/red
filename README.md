# Red

Python Reddit API Wrapper without the hassle.


## Usage

```python
import configparser
from red.auth import authorize
from red.red import Red, OAUTH_ENDPOINT

config = configparser.ConfigParser()
config.read('credentials.ini')
reddit_cred = config['reddit']

access_token = authorize(
    reddit_cred['CLIENT_ID'], 
    reddit_cred['CLIENT_SECRET'],
    reddit_cred['USERNAME'],
    reddit_cred['PASSWORD'],    
)

r = Red(access_token['access_token'])
response2 = r.r_subreddit_search('learnpython', q='why is python')
```