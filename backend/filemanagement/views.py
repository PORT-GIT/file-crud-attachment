from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Logs(request):

    return HttpResponse("Hello world")

def Movement(request):
    return HttpResponse("I am moving")
