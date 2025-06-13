
from django.http import HttpResponse


def Greetings(request):
    return HttpResponse("<h2>Welcome to Django Tutorials...</h2>")

