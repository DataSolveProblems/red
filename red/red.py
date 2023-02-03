import requests
from red.auth import USER_AGENT

OAUTH_ENDPOINT = 'https://oauth.reddit.com'

class User:
    def __init__(self, access_token):
        self.access_token = access_token

    @property
    def headers(self):
        return {
            'User-Agent': USER_AGENT,
            'Authorization': 'Bearer ' + self.access_token
        }    

    def search_user(self, **params):
        """
        https://www.reddit.com/dev/api/oauth#GET_users_search
        """
        response = requests.get(
            OAUTH_ENDPOINT + '/users/search', 
            headers=self.headers,
            params=params
        )
        return response
    
    def user_profile(self, user_id):
        """
        https://www.reddit.com/dev/api/oauth#GET_user_{username}_about
        """
        response = requests.get(
            OAUTH_ENDPOINT + f'/user/{user_id}/about', 
            headers=self.headers,
        )
        return response

    def user_history(self, username, history_type, **params):
        """
        https://www.reddit.com/dev/api/oauth#GET_user_{username}_{where}
        """
        response = requests.get(
            OAUTH_ENDPOINT + f'/user/{username}/{history_type}',
            headers=self.headers,
            params=params
        )
        return response        


class Red:
    def __init__(self, access_token):
        self.access_token = access_token

    @property
    def headers(self):
        return {
            'User-Agent': USER_AGENT,
            'Authorization': 'Bearer ' + self.access_token
        }
    
    def subreddit_post_requirements(self, subreddit):
        """
        https://www.reddit.com/dev/api/oauth#GET_api_v1_{subreddit}_post_requirements
        """
        response = requests.get(
            OAUTH_ENDPOINT + f'/api/v1/{subreddit}/post_requirements',
            headers=self.headers
        )
        return response

    def subreddits(self, where='new', **params):
        """
        https://www.reddit.com/dev/api/oauth#GET_subreddits_{where}
        Get all subreddits.
        """
        response = requests.get(
            OAUTH_ENDPOINT + f'/subreddits/{where}',
            headers=self.headers,
            params=params
        )
        return response

    def search_subreddits(self, **params):
        """
        https://www.reddit.com/dev/api/oauth#GET_subreddits_search
        """
        response = requests.get(
            OAUTH_ENDPOINT + f'/subreddits/search',
            headers=self.headers,
            params=params
        )
        return response        

    def r_subreddit_hot(self, subreddit, **params):
        """
        https://www.reddit.com/dev/api/oauth#GET_hot
        """
        response = requests.get(
            OAUTH_ENDPOINT + f'/r/{subreddit}/hot',
            headers=self.headers,
            params=params
        )
        return response

    def r_subreddit_new(self, subreddit, **params):
        """
        https://www.reddit.com/dev/api/oauth#GET_new
        """
        response = requests.get(
            OAUTH_ENDPOINT + f'/r/{subreddit}/new',
            headers=self.headers,
            params=params
        )
        return response

    def r_subreddit_search(self, subreddit="", **params):
        """
        To limit the search to a specific subreddit,
        set the restrict_sr to True
        e.g. params={'q': 'why is python', 'restrict_sr': 1}

        To search flair:
        e.g. flair:"flair text
        """
        if subreddit:
            endpoint = f'/r/{subreddit}/search'
        else:
            endpoint = '/search'

        response = requests.get(
            OAUTH_ENDPOINT + endpoint,
            # OAUTH_ENDPOINT + f'/r/{subreddit}/search',
            headers=self.headers,
            params=params
        )
        return response    

