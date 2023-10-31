from django.urls import path,re_path
from . import views

#define app name
app_name='pages'

#create url patterns
urlpatterns = [
    path('',views.home, name='home'),
    
]