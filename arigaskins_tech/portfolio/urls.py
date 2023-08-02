from django.urls import path
from . import views

# set urls 
urlpatterns = [
    path('', views.homepage),
]