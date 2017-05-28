#fbAPI -> handles all the stuff related to Facebook.
# All the facebook attributes such as privacy, visibility, etc will be controlled in this class only

from .textToImgConverter import *
from facepy import GraphAPI
from facepy import OAuthError
from facepy import HTTPError
from .commonDefines import *

class FBApi():
	_txtToImgConverter = TextToImageConverter()
	
	def postQuoteAsImg(self, authToken, userName, quote):
		if(quote == ''):
			return [0, RESPONSE_EMPTY_QUOTE]
		graph = GraphAPI(authToken)							#get Graph object of a user
		try:
			response = graph.post(							#post a picture
				path = 'me/photos',							
				source = open(self._txtToImgConverter.convertToImage(quote, userName), 'rb')
				)
		except OAuthError:
			return [0, RES_FB_AUTH_ERR]
		except HTTPError:
			return [0, RES_TRIES_EXCEEDED]
		except OSError:
			return [0, RES_INAVLID_FILE]

		return [1, RES_SUCCESS_POST]

		
