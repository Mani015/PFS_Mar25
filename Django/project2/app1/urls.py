
from django.urls import path
from .views import New_app

urlpatterns = [
    path('app1/',New_app)
]