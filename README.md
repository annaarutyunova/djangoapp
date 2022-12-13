# Overview

An attempt to create a webapp using django on python, to display different objects on the screen and add them to sqlite database in django. 

The purpose of the project is to learn how to build webapps frontend and backend in python using django framework

[Software Demo Video](https://youtu.be/43__pdjOuqk)

# Development Environment

Django
python 3.9.4
Visual Studio Code

# Useful Websites

* [Python Django Documentation](https://docs.djangoproject.com/en/4.1/)


# Future Work

* Actually add more things to the database
* Finish the tutorial

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