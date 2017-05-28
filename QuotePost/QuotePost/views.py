from django.http import *
from django.db import IntegrityError
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.template import Template,Context
from django.template.loader import get_template
from django.contrib.auth.models import User
# Create your views here.

from QuotePost.API.apiMain import APIServices
from QuotePost.API.commonDefines import *

DEFAULT_DIRECTORY_PATH_GUI = "qpost//"

HOMEPAGE_FILE = "homepage.html"

USER_HOMEPAGE_FILE = "login_homepage.html"

_apiServices = APIServices()

def printResponse(dict):
	print("Sending the Response with Following Attributes")
	for key,value in dict.items():
		print(key + " :: " + str(value))
	print("\n")

def sendServicesResponse(dict):
	context = Context(dict)
	printResponse(dict)
	userHomePage = get_template(DEFAULT_DIRECTORY_PATH_GUI + USER_HOMEPAGE_FILE)
	return HttpResponse(userHomePage.render(context))

def home(request):
	if(request.user.is_authenticated()):
		return login_successfull(request)
	homePage = get_template(DEFAULT_DIRECTORY_PATH_GUI + HOMEPAGE_FILE)
	return HttpResponse(homePage.render(Context()))

def login_successfull(request):
	userHomePage = get_template(DEFAULT_DIRECTORY_PATH_GUI + USER_HOMEPAGE_FILE)
	return HttpResponse(userHomePage.render(Context()))

def logout_user(request):
	logout(request)
	return redirect( "http://" + request.META['HTTP_HOST'])
	
def fetchQuote(request):
	result = _apiServices.fetchQuote(request.user.username)
	dict = {
			'error_flag' : str(result[IS_SUCCESSFULL]^1) ,
			'quote' : result[RETURN_STRING]
			}
	return sendServicesResponse(dict)
	
def saveQuote(request):
	result = _apiServices.saveQuote(request.user.username, request.GET['quote'] )
	dict = {
			'error_flag' : str(result[IS_SUCCESSFULL]^1) ,
			'message' : result[RETURN_STRING]
		}
	return sendServicesResponse(dict)

	
def postQuote(request):
	social = request.user.social_auth.get(provider='facebook')
	result = _apiServices.postQuote(request.user.username, request.GET['quote'], social.extra_data['access_token']  )
	
	dict = {
					'error_flag' : str(result[IS_SUCCESSFULL]^1) ,
					'message' : result[RETURN_STRING]
						}
	return sendServicesResponse(dict)

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