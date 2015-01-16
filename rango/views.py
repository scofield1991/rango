from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context_dict={'boldmessage': "I am bold font from the context"}
    return render(request,'rango/index.html', context_dict )

def about(request):
    return HttpResponse("Rango says here is about page <a href='/rango/'>Index</a>")
