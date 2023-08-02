from django.urls import path
from . import views

# set urls 
urlpatterns = [
    path('', views.homepage),
    path('work-history/', views.work_history),
    path('certifications/', views.certifications),
    path('alma-maters/', views.alma_maters),
]