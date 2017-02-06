from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegistrationForm, LoginForm
from django.contrib import messages

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm(request.POST or None)
        context = {
            "form":form,
            "title":"Register"
        }

        return render(request, 'accounts/register.html', context)

    def post(self,request):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = user.password
            user.set_password(password)
            user.save()

            user = authenticate(username=user.username, password=password)
            login(request, user)
            messages.success(request,"Succesfully Registered")
            return redirect('user:update_profile',user.username)
        context={
            "form":form,
            "title":"Register"
        }
        return render(request, 'accounts/register.html', context)


class LoginView(View):
    def get(self, request):
        form = LoginForm(request.POST or None)
        context = {
            "form":form,
            "title":"Login"
        }
        return render(request, 'accounts/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request,user)
                messages.success(request,"Logged In Succesfully")
                return redirect('home')

        messages.warning(request,"Invalid Username/Password")
        context = {
            "form":form,
            "title":"Login"
        }
        return render(request, "accounts/login.html", context)

class LogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"Logged Out Succesfully")
        return redirect('home')
