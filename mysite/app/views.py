# from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def index(request):
    return HttpResponse("Hello, world")
def index(request):
    # filter item_name by alphabet
    alph_items = Item.objects.order_by('item_name')
    output = ', '.join([a.item_name for a in alph_items])
    return HttpResponse(output)

def detail(request, item_id):
    return HttpResponse("You're looking at item %s." %item_id)

def results(request, item_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % item_id)