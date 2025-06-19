from django.shortcuts import render
from app5.models import Student
# Create your views here.

def Student_info(request):
    stu = Student.objects.all()  # SELECT * FROM TABLE_NAME;
    return render(request,'stu.html',{'stu' : stu})