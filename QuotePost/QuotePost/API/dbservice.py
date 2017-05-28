# dbservice - handles all the dbservices and acts as a wrapper around DB.
# Maintains all the constraints
# if fails returns accordingly 


from quotes.models import *
from .commonDefines import *
from django.db import Error
from django.db import transaction

class DBServices():
	
	#dictionary of all the users logged in mapped to the dictionary of all the quotes they have saved
	#used to check whether the quote is already fetched or not.
	_fetchedQuotes = {'':{}}
	
	#saves the quote 
	def saveQuote(self, userName , quote, isPosted):
		quote = ' '.join(quote.strip().split())										#removes multiple spaces
		if(quote == ''):															#empty quote check
			return [0, RESPONSE_EMPTY_QUOTE]
		rows = Quotes.objects.filter(userName = userName , quote__iexact = quote)			
		if( rows.count() > 0 ):														#check if already saved
			if(rows[0].isAlreadyPosted == False and isPosted == True ):
				rows[0].isAlreadyPosted = True
				rows[0].save()
				return [1, RES_QUOTE_UPDATED_IN_DB]
			return [0, RESPONSE_ALREADY_SAVED_QUOTE]
		else:
			try:																	#save the quote
				Quotes(userName = userName , quote = quote, isAlreadyPosted = isPosted).save()
			except Error:
				return[0, RESPONSE_SAVE_QUOTE_FAIL]
		return [1, RESPONSE_SUCCESS_SAVE]
	
	def fetchQuote(self,userName):
		quotesToSend = Quotes.objects.filter(userName = userName, isAlreadyPosted = False)					#find all quotes of user
		
		if( quotesToSend.count() == 0 ):
			return [0, RES_NO_SAVED_QUOTES, 0]
		
		if( userName not in self._fetchedQuotes.keys()):							#user first time fethces
			self._fetchedQuotes[userName] = {}
		
		userMap = self._fetchedQuotes[userName]										
		for quote in quotesToSend:													#check if already present in fetched quote map
			if(quote not in userMap.keys()):
				self._fetchedQuotes[userName][quote] = 1							#update the map
				return [1, quote, 1]
		
		self._fetchedQuotes[userName].clear()
		return [0, RESPONSE_ALL_QUOTES_FETCHED, 0]									#return

#tells whether the quote is already Posted or not		
	def isQuoteAlreadyPosted(self,userName,quote):
		rows = Quotes.objects.filter(userName = userName , quote__iexact = quote)
		if(rows.count() > 0):
			return rows[0].isAlreadyPosted
		return False;	
		
#fill the db with  HardCoded Entries for the purpose of Testing
	def fillDB(self):
		Quotes.objects.all().delete()
		quotes = [ "My Quote iS Savage, But You Aint gonna get it.",
			"My life is like Black & White",
			"When Nothing goes Right Go Left."
			]
		userNames = [ 'BettyAlagfbejcaeeiYangman' , 'MariaAlagfacccbibdMartinazzisen' , 'JohnAlageebhbhafgBharambesky' ]

		j = 1
		print("Adding Entries to DB")
		with transaction.atomic():
			for user in userNames:
				for i in range(1,1000):
					Quotes(userName = user, quote = str(j) + "." + quotes[i%3], isAlreadyPosted = False).save()
					j = j + 1

		transaction.commit()
		return [1, "Completed process : Entered " + str(j) + " Entries"]
	