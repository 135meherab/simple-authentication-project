from django.shortcuts import render, redirect
from . user_change_data import ChangeUserData
from django.contrib import messages
# Create your views here.
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request,"Account Updated Successfully")
                form.save()
        else:
            form = ChangeUserData(instance = request.user)
        
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('login_page')

 