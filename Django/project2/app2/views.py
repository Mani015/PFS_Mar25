from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def AppView(request):

    return HttpResponse("<h1>This view is coming from app level folder</h1>")


