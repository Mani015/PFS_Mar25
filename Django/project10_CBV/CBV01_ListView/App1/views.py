from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView
from App1.models import Product

# Create your views here.

# class Greetings(View):
#     def get(self,request):
#         return HttpResponse('<h1>Welcome to class based views</h1>')


class ProductListView(ListView):
    model = Product
    # By default template name is product_list.html
    # By default context_name product_list

