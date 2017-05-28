#QuotePost

Requirements 
	python 3.4
	virtualenv

Deployement Steps
1. virtualenv env
2. activate env
4. git clone <Remote>
3. pip install requirements.pip
4. cd QuotePost/QuotePost
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver

Note: Always use localhost:8000 instead of 10.0.0.30:8000 as I have registered localhost:8000 as the \
domain of the app on facebook.

if you have issues with the deployement please feel free to contact me at 8146521550