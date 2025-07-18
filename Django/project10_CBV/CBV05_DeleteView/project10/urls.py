"""
URL configuration for project10 project.

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
from App1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.Greetings)?: (urls.E009) Your URL pattern '' has an invalid view, pass Greetings.as_view() instead of Greetings.
    # path('',views.Greetings.as_view())
    path('',views.ProductListView.as_view(),name='pro2'),
    path('<int:pk>/',views.ProductDetailView.as_view(),name='pro1'),
    path('create/',views.ProductCreateView.as_view()), # No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
    path('update/<int:pk>/',views.ProductUpdateView.as_view()),
    path('delete/<int:pk>/',views.ProductDeleteView.as_view())






]
