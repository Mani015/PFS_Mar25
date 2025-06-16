from django.shortcuts import render
import datetime
# Create your views here.

def Basic_template(request):

    # render(request, template_path,context = dict)
    return render(request,'basic.html')



def Current_date(request):
    showtime = datetime.datetime.now()
    return render(request,'datetime.html',{'date' : str(showtime)})



