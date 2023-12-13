from django.shortcuts import render,redirect
from . reg_form import RegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                form.save()
                messages.success(request,"Account created successfully")
        else:
            form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    else:
        return redirect('profile_page')