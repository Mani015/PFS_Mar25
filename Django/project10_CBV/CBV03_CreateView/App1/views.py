from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView
from App1.models import Product

# Create your views here.

# class Greetings(View):
#     def get(self,request):
#         return HttpResponse('<h1>Welcome to class based views</h1>')


class ProductListView(ListView):
    model = Product
    # By default template name is product_list.html
    # By default context_name product_list

class ProductDetailView(DetailView):
    model = Product
    # By default template name is product_detail.html
    # BY default context name product

class ProductCreateView(CreateView):
    model = Product
    # fields = ('Pname','Pprice')
    fields = '__all__'
    # By default template name is product_form.html
    # BY default context name form



