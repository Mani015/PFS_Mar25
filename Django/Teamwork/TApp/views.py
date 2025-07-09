from django.shortcuts import render
from TApp.models import Student
from TApp.forms import Studentform
# Create your views here.

def Team_list(request):
    stu=Student.objects.all()
    return render(request,'list.html',{'stu':stu})


def TForm(request):
    form_key = Studentform()
    if request.method=='POST':
        new = Studentform(request.POST)
        if new.is_valid():
            new.save()
            return Team_list(request)
    return render(request,'form.html',{'form_key':form_key})
