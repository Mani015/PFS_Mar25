from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def New_app(reuqest):

    return HttpResponse("<h1>This view is coming from app1 level folder</h1>")
