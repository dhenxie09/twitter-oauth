from requests_oauthlib import OAuth1Session


class TwitterOAuth(object):
    def __init__(self, consumer_key=None, consumer_secret=None):
        self._request_token_url = "https://api.twitter.com/oauth/request_token"
        self._oauth_token_url = "https://api.twitter.com/oauth/access_token"
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
    
    def request_token(self):
        request_token = OAuth1Session(
            client_key=self._consumer_key,
            client_secret=self._consumer_secret
        )

        data = request_token.get(self._request_token_url)
        data_token = data.text.split('&')
        ro_key = data_token[0].split('=')
        ro_secret = data_token[1].split('=')
        self.resource_owner_key = ro_key[1]
        self.resource_owner_secret = ro_secret[1]

        return {
            "resource_owner_key": self.resource_owner_key,
            "resource_owner_secret": self.resource_owner_secret
        }
    
    def get_oauth_token(self, verifier, ro_key, ro_secret):
        oauth_token = OAuth1Session(client_key=ro_key,
                            client_secret=ro_secret,
                            resource_owner_key=ro_key,
                            resource_owner_secret=ro_secret)
        data = {"oauth_verifier": verifier}
        access_token_data = oauth_token.post(self._oauth_token_url, data=data)
        print(access_token_data.text)
        access_token_list = access_token_data.text.split('&')
        oauth_token = access_token_list[0].split("=")[1]
        oauth_token_secret = access_token_list[1].split("=")[1]

        return {
            "oauth_token": oauth_token,
            "oauth_token_secret": oauth_token_secret
        }
