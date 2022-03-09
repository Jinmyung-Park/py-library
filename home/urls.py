from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.Login.as_view(), name='login'),
    path('home/', views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/',views.logout, name='logout'),
]

