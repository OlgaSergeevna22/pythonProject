from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    task=Task.objects.all()
    return render(request, 'main/index.html',{'title':'Главная страница','tasks':task})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == "POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была не верной'
    form=TaskForm()
    context={
        'form':form,
        'error':error
    }
    return render(request, 'main/create.html',context)

def feedback(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/feedback.html',context)


