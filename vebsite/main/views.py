from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def home(request):
    return HttpResponse('<h2>HomeWork</h2>')

def new(request):
    return render(request, 'new_page.html')

