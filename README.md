# py -m venv venv
# create a test.py file in the root level
# activate the environment
# django-admin startproject mysite(mysite is the name of the project)
# cs into mysite
# run python manage.py startapp app (app is the name)
# python manage.py runserver
# go to app/views.py 
# from django.http iport HttpResponse
# def index(request):
# return HttpResponse("Hello, world") 
# create urls.py in app folder
# in app/urls.py
# from django.urls import path
# from . import views
# urlpatterns = [path('', views.index, #name='index'),] 
# for further reference use https://docs.djangoproject.com/en/4.1/intro/tutorial01/ and
# https://docs.djangoproject.com/en/4.1/intro/tutorial01/