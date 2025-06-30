
from django.urls import path
from .views import AppView


urlpatterns = [
    path('app2/',AppView)
]