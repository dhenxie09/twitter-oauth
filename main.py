from twitter import TwitterOAuth

def request_token(consumer_key, consumer_secret):
    twitter_oauth = TwitterOAuth(
        consumer_key=consumer_key, consumer_secret=consumer_secret
    )

    response = twitter_oauth.request_token()
    oauth_token = None
    oauth_token_secret = None

    result = {
        "success": True,
        "data": {},
        "code": 200
    }

    try:
        oauth_token = response.get("resource_owner_key", "")
        oauth_token_secret = response.get("resource_owner_secret", "")

        result.update({
            "data": {
                "oauth_token": oauth_token,
                "oauth_token_secret": oauth_token_secret
            }
        })
    except Exception, e:
        result = {
            "success": False,
            "message": "Something went wrong.",
            "code": 401
        }

    return result


def get_oauth_token(consumer_key, consumer_secret, oauth_verifier, oauth_token, oauth_token_secret):
    twitter_oauth = TwitterOAuth(
        consumer_key=consumer_key, consumer_secret=consumer_secret
    )

    response = twitter_oauth.get_oauth_token(
        oauth_verifier,
        oauth_token,
        oauth_token_secret
    )

    result = {
        "success": True,
        "data": {},
        "code": 200
    }

    try:
        result.update({
            "data": response
        })
    except Exception, e:
        result = {
            "success": False,
            "message": "Something went wrong.",
            "code": 401
        }

    return result   


def logout(consumer_key, consumer_secret, oauth_token, oauth_token_secret):
    twitter_oauth = TwitterOAuth(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret
    )

    response = twitter_oauth.logout(
        oauth_token,
        oauth_token_secret
    )

    result = {
        "success": True,
        "data": {},
        "code": 200
    }

    try:
        result.update({
            "data": response
        })
    except Exception, e:
        result = {
            "success": False,
            "message": "Something went wrong.",
            "code": 401
        }

    return result    


def main(
        consumer_key, consumer_secret, method,
        oauth_verifier=None, oauth_token=None,
        oauth_token_secret=None):
    result = {}

    if method == "request_token":
        result = request_token(consumer_key, consumer_secret)
    
    if method == "get_oauth_token":
        result = get_oauth_token(
            consumer_key,
            consumer_secret,
            oauth_verifier,
            oauth_token,
            oauth_token_secret
        )
    
    if method == "logout":
        result = logout(
            consumer_key,
            consumer_secret,
            oauth_token,
            oauth_token_secret
        )

    return result
