# QuotePost - views

#
# This module handles the RequesT and responses and is responsible for the authentication of a user via facebook
# dependent on python social auth and django social auth.
# views directly do not handle the service
# it has an APIServices object which does the work and views then send it as a response.
# It has nothing to do with the internal structure of API Service or any other module for that matter.
# They act as a black box for views.

#Functions
#1. authentication
#2. handling request and responses.  


from django.http import *
from django.db import IntegrityError
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.template import Template,Context
from django.template.loader import get_template
from django.contrib.auth.models import User

from QuotePost.API.apiMain import APIServices
from QuotePost.API.commonDefines import *

#directory path where HTML templates are present.
DEFAULT_DIRECTORY_PATH_GUI = "qpost//"

#name of the homepage HTML file
HOMEPAGE_FILE = "homepage.html"

#name of the user_specific homepage file after login
USER_HOMEPAGE_FILE = "login_homepage.html"

#keys in dict that will be sent as a response
DICT_KEY_ERROR_FLAG = 'error_flag'
DICT_KEY_MESSAGE = 'message'
DICT_KEY_QUOTE = 'quote'

#APIServices object .All the functions that needs to be performed will be called via this object only.
_apiServices = APIServices()


#printResponse(dict) - print the dict that is being sent as a response
def printResponse(dict):
	print("Sending the Response with Following Attributes")
	for key,value in dict.items():
		print(key + " :: " + str(value))
	print("\n")

#sendServicesResponse(dict) - sends the response in case of fetch save and post to fb services. 
def sendServicesResponse(dict):
	context = Context(dict)
	printResponse(dict)
	userHomePage = get_template(DEFAULT_DIRECTORY_PATH_GUI + USER_HOMEPAGE_FILE)
	return HttpResponse(userHomePage.render(context))

#sends the launching login page	
#if user is logged in it will send user homepage
def home(request):
	if(request.user.is_authenticated()):
		return login_successfull(request)
	homePage = get_template(DEFAULT_DIRECTORY_PATH_GUI + HOMEPAGE_FILE)
	return HttpResponse(homePage.render(Context()))

#send users homepage
def login_successfull(request):
	userHomePage = get_template(DEFAULT_DIRECTORY_PATH_GUI + USER_HOMEPAGE_FILE)
	return HttpResponse(userHomePage.render(Context()))

#logout a user and redirect to homepage.
def logout_user(request):
	logout(request)
	return redirect( "http://" + request.META['HTTP_HOST'])

#fetches quote from database
def fetchQuote(request):
	print("\n RECIEVED FETCH QUOTE FROM DB REQUEST WITH FOLLOWING ARGUMENTS: ")
	print("Username:" + request.user.username)
	result = _apiServices.fetchQuote(request.user.username)
	dict = {
			DICT_KEY_ERROR_FLAG : str(result[IS_SUCCESSFULL]^1) ,
			}
	if(result[IS_QUOTE]):
		dict[DICT_KEY_QUOTE] = result[RETURN_STRING]
	else:
		dict[DICT_KEY_MESSAGE] = result[RETURN_STRING]
		
	return sendServicesResponse(dict)

#saves quote in database
def saveQuote(request):
	print("\n RECIEVED SAVE QUOTE TO DB REQUEST WITH FOLLOWING ARGUMENTS: ")
	print("Username:" + request.user.username)
	print("Quote:"    + request.GET['quote'])
	result = _apiServices.saveQuote(request.user.username, request.GET['quote'] )
	dict = {
			DICT_KEY_ERROR_FLAG : str(result[IS_SUCCESSFULL]^1) ,
			DICT_KEY_MESSAGE : result[RETURN_STRING]
		}
	return sendServicesResponse(dict)

#post quote to fb
def postQuote(request):
	print("\n RECIEVED POST QUOTE TO FB REQUEST WITH FOLLOWING ARGUMENTS: ")
	print("Username:" + request.user.username)
	print("Quote:"    + request.GET['quote'])
	social = request.user.social_auth.get(provider='facebook')
	result = _apiServices.postQuote(request.user.username, request.GET['quote'], social.extra_data['access_token']  )
	
	dict = {
				DICT_KEY_ERROR_FLAG : str(result[IS_SUCCESSFULL]^1) ,
				DICT_KEY_MESSAGE : result[RETURN_STRING]
			}
	return sendServicesResponse(dict)

	
#this is the function that is called on pressing either of the three buttons
#fetch save and post
#it checks whether the user is logged in or not
#if logged in sends appropriate response.

def submitForm(request):
	if(request.user.is_authenticated()):
		if( 'fetch' in request.GET ):
			return fetchQuote(request)
		elif('save' in request.GET):
			return saveQuote(request)
		else:
			return postQuote(request)
	else:
		return redirect( "http://" + request.META['HTTP_HOST'])
		
		
def fillDB(request):
	res =  _apiServices.fillDB()
	return HttpResponse(res[RETURN_STRING])