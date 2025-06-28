from django.shortcuts import render,redirect
from app8.models import EmployeeModel
from app8.forms import EmployeeForm
# Create your views here.

def EmpList(request):
    emp = EmployeeModel.objects.all()
    return render(request,'list.html',{'emp' : emp})

#Create
def EmpForm(request):
    form = EmployeeForm()
    if request.method == 'POST':
        new = EmployeeForm(request.POST)
        if new.is_valid():
            new.save()
            return EmpList(request)
    return render(request,'form.html',{'form' : form})


# Update
def EmpUpdate(request,id):
    emp_id = EmployeeModel.objects.get(id = id)
    if request.method == 'POST':
        emp = EmployeeForm(request.POST,instance = emp_id)
        if emp.is_valid():
            emp.save()
            return redirect('/')
    return render(request,'update.html',{'emp_id' : emp_id})


# Delete

def EmpDelete(request,id):
    emp_data = EmployeeModel.objects.get(id = id)
    emp_data.delete()
    return redirect('/')

