#custom facebook backend - needed to get publish_actions request from user otheriwse
#we wont be able to post to facebook on behalf of users

from social.backends.facebook import FacebookOAuth2

class CustomFacebookOAuth2(FacebookOAuth2):
    def get_scope(self):
        scope = super(CustomFacebookOAuth2, self).get_scope()  #get scope
        scope = scope + [('publish_actions')]				   #append 'publish_actions' to scope
        return scope