#QuotePost

Pre - Requirements: 
	python 3.4
	virtualenv
	
Deployement Steps on a window machine:
In Command Prompt write following commands
1. virtualenv env
2. env\Scripts\activate
3. Go to directory where you have cloned the source
4. pip install -r requirements.txt ( might take around 15-20 mins  to download and install)
5. cd QuotePost
6. python manage.py makemigrations
7. python manage.py migrate
8. python manage.py runserver
9. go to browser to address localhost:8000/filldb It will populate your db with around 300 entries

the server will run at localhost:8000

####NOTE: Always use localhost:8000 instead of 10.0.0.30:8000 as I have registered localhost:8000 as the 
domain of the app on facebook.

TEST CLIENT CREDENTIALS ON Facebook
email1 : eibutrzbjd_1495954063@tfbnw.net
email2 : owhybykhnu_1495954061@tfbnw.net
email3 : yzuwypejje_1495954059@tfbnw.net
password : mirrors23 (for all the above accounts)

if you have issues with the deployment please feel free to contact me at 8146521550

FUNCTIONS:
1. fetch unique quotes from DB once all quotes are fetched . "All favourites quotes fetched" will appear on screen and the cycle will start again
2. Save Quotes to DB for fetching later
3. Post The Quote in the field to Fb as an image with random background and quote in middle in white color.