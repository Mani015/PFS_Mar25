from django.shortcuts import render

# Create your views here.

def Basic_template(request):

    # render(request, template_path,context)
    return render(request,'basic.html')

