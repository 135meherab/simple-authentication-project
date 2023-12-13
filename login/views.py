from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login 
from django.contrib import messages

# Create your views here.
def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request= request, data= request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username = name, password = user_pass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Logged In Successfully')
                    return redirect('profile_page')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html',{'form':form})
    else:
        return redirect('profile_page')