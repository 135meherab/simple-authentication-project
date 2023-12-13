from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def change_with_old(request):
    if request.method == 'POST':
        form  = PasswordChangeForm(user=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile_page')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'update_pass.html', {'form':form})

def change_without_old(request):
    if request.method == 'POST':
        form  = SetPasswordForm(user=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile_page')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'update_pass2.html', {'form':form})