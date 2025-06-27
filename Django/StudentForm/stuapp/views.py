from django.shortcuts import render
from stuapp import forms
from stuapp.models import StudentModel
# Create your views here.


def StudentList(request):
    stu = StudentModel.objects.all()
    return render(request,'list.html',{'stu_list' : stu})


def StudentForm(request):
    form = forms.Student()
    if request.method == 'POST':
        stu_form = forms.Student(request.POST)
        if stu_form.is_valid():
            stu_form.save()
            return index(request)
    return render(request,'form.html',{'form' : form})



def index(request):
    return render(request,'index.html')
