from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# HTTP (hyper text Transfer), http is a stateless protocol,if a protocol is a statelss
# it means the server doesn't maintain a continues Connection server
# because socket connection is alived  every time it destroys
# {HTTP is a short term memory loss}
#
# Scalability: There are no.of scability server different app ,different web server,
# they are not work on the same server
#
# session tracking:To maintain a state despite the stateles of HTTP
# ex:You are maintain a e cart application to main server management.
#
# waht is session?: A session can be defined two ways[login & logout]
# ex: facebook, instragram, Gmail,
# thhis apps going to everything happen this login & logout
#
# Track user intraction:
# suppose they are accesing the web site  from that till close your browser or
# leave that website is called user interaction
# ex: My book show tickets, e-commerce
#
# Cookies support:
# 1).request.session ---->set_test_cookie()
# 2).request.session ---->test_cookie_worked()
# 3).request.session ---->delete_test_cookie()


def Home(request):
    request.session.set_test_cookie()  # # Exception Value:	no such table: django_session
    return HttpResponse('<p>THis is Home Page : Set a Cookie In the broswer By defaultly</p>')


def Page2(request):
    if request.session.test_cookie_worked():
        print('Cookies Are enabled ')  # return in Server page or django console page
        request.session.delete_test_cookie()
    return HttpResponse('<p>Page2</p>')


