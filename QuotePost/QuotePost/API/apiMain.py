
from .dbservice import DBServices
import importlib
importlib.reload
from .fbApi import FBApi
from .commonDefines import *

class APIServices():
	_dbService = DBServices()
	_fbApi = FBApi()
	
	def fetchQuote(self, userName):
		return self._dbService.fetchQuote(userName);
		
	def saveQuote(self, userName, quote):
		return self._dbService.saveQuote(userName, quote, False);
		
	def postQuote(self, userName, quote, authToken):
		if( self._fbApi.postQuoteAsImg(authToken, userName, quote)[IS_SUCCESSFULL] == 1  ):
			
			if ( self._dbService.saveQuote(userName, Quote, True)[IS_SUCCESSFULL] == 1 ):
				return [1, "Quote Saved And Posted Successfully."]
			else:
				return [0, "Posted to facebook , Unable to Save Quote. "]
				
		else:
			return [False, "Unable to Post the Quote to Facebook."]
			
		