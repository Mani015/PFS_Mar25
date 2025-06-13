from django.http import HttpResponse
def Create_fun(request):

    return HttpResponse("<h3>This view is coming from view1 module</h3>")

