from .textToImgConverter import *
from facepy import GraphAPI
from facepy import OAuthError
from facepy import HTTPError

class FBApi():
	_txtToImgConverter = TextToImageConverter()
	
	def postQuoteAsImg(self, authToken, userName, quote):
		graph = GraphAPI(authToken)
		try:
			response = graph.post(
				path = '',
				source = open(self._txtToImgConverter.convertToImage(quote, userName), 'rb'),
				retry = 10
				)
		except OAuthError:
			return [0, "Cannot Post the Quote because The Apps are not allowed to past on behalf of user unless allowed by the user"]
		except HTTPError:
			return [0, "We have exceeded the number of tries to save photos."]
			
		if(response['success']):
			return [1,"Your Quote has been successfully posted to your facebook timeline"]
		else:
			return [0, response['success']]

		
