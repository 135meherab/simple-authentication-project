from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('home_page')