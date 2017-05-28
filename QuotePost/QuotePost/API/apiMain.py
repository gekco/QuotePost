#apiMain 

#apiMain contains all the function that can be called as a RPC from web.
#currently it can do following tasks
#1. fetch quotes
#2. save quotes recieved from user
#3. post quote to fb and save it.


from .dbservice import DBServices
from .fbApi import FBApi
from .commonDefines import *

class APIServices():
	
	#dbservice handles all the aspect of Database and acts as a warapper around db calls.
	#all the constraints are handled inside _dbService like(unique quote every time)
	_dbService = DBServices()
	
	#fbApi - as the name suggests connect us to facebook and lets us do all the operations on behalf of the user
	_fbApi = FBApi()
	
	#fetchQuote - fetches Quote from db - new one each time
	def fetchQuote(self, userName):
		return self._dbService.fetchQuote(userName);
		
	#saveQuote - save quote to DB 
	def saveQuote(self, userName, quote):
		return self._dbService.saveQuote(userName, quote, False);
	
	#post quote to Fb
	def postQuote(self, userName, quote, authToken):
		quote = ' '.join(quote.strip().split(' '))                                                          #remove multiple spaces in quotes
		if(not self._dbService.isQuoteAlreadyPosted(userName, quote)):
			response = self._fbApi.postQuoteAsImg(authToken, userName, quote)								#check if quote already posted
			if( response[IS_SUCCESSFULL] == 1  ):
				responseSave = self._dbService.saveQuote(userName, quote, True)								#post quote as img
				if ( responseSave[IS_SUCCESSFULL] == 1 ):               #save quote  
					return [1, RESPONSE_QUOTE_POST_SAVE_SUCCESS]
				else:
					return [0, RESPONSE_FB_POST_FAIL]
			else:
				return response
		return [0, RESPONSE_QUOTE_ALREADY_POSTED]															#return appropriate error 			
		