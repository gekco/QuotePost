from quotes.models import *
from .commonDefines import *

class DBServices():
	
	_fetchedQuotes = {'':{}}
	
	def saveQuote(self, userName , quote, isPosted):
		rows = Quotes.objects.filter(userName = userName , quote = quote)
		if( rows.count() > 0 ):
			return [0, "You have Already Saved This Quote"]
		else:
			Quotes(userName = userName , quote = ' '.join(quote.strip().split()), isAlreadyPosted = isPosted).save()
		return [1, "Successfully Saved"]
	
	def fetchQuote(self,userName):
		quotesToSend = Quotes.objects.filter(userName = userName)
		
		if( userName not in self._fetchedQuotes.keys()):
			self._fetchedQuotes[userName] = {}
		
		userMap = self._fetchedQuotes[userName]
		for quote in quotesToSend:
			if(quote not in userMap.keys()):
				self._fetchedQuotes[userName][quote] = 1
				return [1, quote]
		
		_fetchedQuotes.clear()
		return [0, "All Favourite Quotes Fetched Already."]
				
			
