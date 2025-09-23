from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# functions

# views.index

def index(request):
    return HttpResponse("<h1>Hello world!</h1>")

# views.about

def about(request):
    return render(request, 'pages/about.html')
