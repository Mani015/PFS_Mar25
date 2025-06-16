from django.shortcuts import render

# Create your views here.

def Profile1(request):
    My_info = {
        'Name' : 'Sai charan',
        'Age' : 22,
        'Salary' : 60000

    }
    return render(request,'info.html',My_info)


def Profile2(request):
    My_info = {
        'Name' : 'chandra hassan',
        'Age' : 24,
        'Salary' : 70000

    }
    return render(request,'info.html',My_info)


def Profile3(request):
    My_info = {
        'Name' : 'Sai kumar',
        'Age' : 25,
        'Salary' : 80000

    }
    return render(request,'info.html',My_info)


def Index(request):
    return render(request,'index.html')
