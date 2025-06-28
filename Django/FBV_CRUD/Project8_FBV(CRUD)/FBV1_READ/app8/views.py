from django.shortcuts import render
from app8.models import EmployeeModel
# Create your views here.

def EmpList(request):
    emp = EmployeeModel.objects.all()
    return render(request,'list.html',{'emp' : emp})


