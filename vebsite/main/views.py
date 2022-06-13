from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h4>hello</h4>')

def home(request):
    return HttpResponse('<h2>HomeWork</h2>')

def new(request):
    return render(request, 'new_page.html')

