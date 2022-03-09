from home.forms import UserForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

@login_required
def home(request):
    return render(request, 'home.html',{})

class Login(LoginView):
    
    template_name = "title.html"

    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home:home')
        else:
            return render(request,'title.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email =request.POST['email'],
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:home')
    else:
        form = UserForm
    return render(request, 'title.html', {'form': form})

def logout(request):
    request.session.flush()
    return redirect('/')