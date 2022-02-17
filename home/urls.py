from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',auth_views.LoginView.as_view(template_name='layouts/app.html'),name='login'),
    path('home', views.home,name='home'),
]

