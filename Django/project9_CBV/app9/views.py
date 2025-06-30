from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,ListView,DetailView,UpdateView,DeleteView,CreateView
# Create your views here.

class Invite(View):

    def get(self,request):
        return HttpResponse("<h2>Welcome to Class Based Views</h2>")

