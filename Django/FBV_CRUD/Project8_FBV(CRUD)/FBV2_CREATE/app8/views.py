from django.shortcuts import render
from app8.models import EmployeeModel
from app8.forms import EmployeeForm
# Create your views here.

def EmpList(request):
    emp = EmployeeModel.objects.all()
    return render(request,'list.html',{'emp' : emp})


def EmpForm(request):
    form = EmployeeForm()
    if request.method == 'POST':
        new = EmployeeForm(request.POST)
        if new.is_valid():
            new.save()
            return EmpList(request)
    return render(request,'form.html',{'form' : form})
