"""
URL configuration for project9_CBV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app9 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.Invite.as_view())
    path('',views.VoterListView.as_view(),name = 'vote2'),
    path('<int:pk>/',views.VoterDetailView.as_view(),name = 'vote1'), # #Reverse for 'vote1' not found. 'vote1' is not a valid view function or pattern name.
    path('create/',views.VoterCreateView.as_view()),
    path('update/<int:pk>/',views.VoterUpdateView.as_view()),
    path('delete/<int:pk>/',views.VoterDeleteView.as_view())

]

